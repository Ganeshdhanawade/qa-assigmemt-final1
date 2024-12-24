import mlflow
from mlflow.tracking import MlflowClient
from transformers import AutoModelForDocumentQuestionAnswering, AutoTokenizer, pipeline
import torch
import os

#path where the train model will be saved
MODEL_PATH = "models/saved_model"
MLFLOW_TRACKING_URI = "http://localhost:5000"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


def retrain_model(data_path):
    """retrain model and log to the mlflow"""
    with mlflow.start_run:
        mlflow.log_artifact(data_path)

        #load the llama model
        model_name = "meta-llama/Llama-2-7b-hf"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForDocumentQuestionAnswering.from_pretrained(model_name)

        # Simulate training (here you would add the actual retraining code)
        # For simplicity, we directly use the pre-trained model as a placeholder
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

        #log train model
        mlflow.pyfunc.log_model("qa_model", python_model=qa_pipeline)

        #log parameters and metrics
        mlflow.log_param("Model_name",model_name)
        mlflow.log_metric("accuracy", 0.95)

        print("Model training and logging completed.")


def monitor_model():
    """ monitor the model performance and verstion using MLflow."""
    client = MlflowClient(MLFLOW_TRACKING_URI)
    latest_run = client.search_runs(order_by=['start_time desc'])[0]
    model_version = latest_run.data.params.get("model_name")
    accuracy = latest_run.data.metrics.get("accuracy")

    print(f"Latest Model Version: {model_version}")
    print(f"Model Accuracy: {accuracy}")

