# MLOps Pipeline

This repository implements a complete Machine Learning Operations (MLOps) pipeline for training, deployment, and monitoring of machine learning models.

---

---

## Overview
This project automates the lifecycle of a machine learning model, from training and versioning to deployment and monitoring. It ensures reproducibility, scalability, and continuous improvement of the model.

---

## Architecture
![MLOps Architecture](https://github.com/Ganeshdhanawade/qa-assigmemt-final1/blob/main/1_ub_u88a4MB5Uj-9Eb60VNA.jpg))

The pipeline consists of three major stages:
1. **Training**: Data preparation, model training, and versioning.
2. **Deployment**: Model packaging into a container and deploying as an API service.
3. **Monitoring**: Tracking model performance and detecting data or performance drift.

---

## Features
- Data versioning with **DVC** and storage on **AWS S3**.
- Model tracking and logging with **MLflow**.
- Deployment using **Docker** and **AWS ECS**.
- Real-time monitoring using **Evidently AI**.

---

## Technologies Used
- **Programming Language**: Python
- **Data Versioning**: DVC, AWS S3
- **Model Tracking**: MLflow
- **Containerization**: Docker
- **Deployment**: AWS ECS
- **Monitoring**: Evidently AI
- **Web Framework**: FastAPI

---

## Setup Instructions
### 1. Prerequisites
- Python 3.8 or later
- Docker
- AWS CLI configured with your account
- DVC installed (`pip install dvc`)
- MLflow installed (`pip install mlflow`)
- FastAPI and Uvicorn (`pip install fastapi uvicorn`)

### 2. Clone the Repository
```bash
git clone https://github.com/your-repo/mlops-pipeline.git
cd mlops-pipeline
```

# Retrieval-Augmented Generation (RAG) Pipeline with Milvus and GPT-Neo

This project implements a Retrieval-Augmented Generation (RAG) pipeline for querying enterprise knowledge bases using vector embeddings stored in **Milvus**, combined with a **GPT-Neo (EleutherAI/gpt-neo-1.3B)** language model to generate responses. The pipeline is deployed using **FastAPI** and containerized with **Docker**.

## Overview

The RAG pipeline ingests documents, preprocesses them, generates vector embeddings using `sentence-transformers/all-MiniLM-L6-v2`, and stores the embeddings in **Milvus**. A user query retrieves the top 3 most relevant documents, enhances the context, and generates a response using **GPT-Neo**. The system is designed to handle large-scale document retrieval and real-time response generation.

---

## Pipeline Architecture

![RAG Pipeline Architecture](https://github.com/Ganeshdhanawade/qa-assigmemt-final1/blob/main/rag-pipeline.png)

### Steps in the Pipeline:
1. **Document Ingestion**:
   - Documents (e.g., PDFs) are preprocessed into chunks.
   - Vector embeddings for the chunks are generated using `sentence-transformers/all-MiniLM-L6-v2`.
   - Embeddings are stored in **Milvus**, a vector database.

2. **Query and Response Generation**:
   - User queries are embedded and compared with the stored document embeddings in Milvus.
   - The top 3 relevant document chunks are retrieved.
   - A prompt is created by combining the query and retrieved context.
   - The prompt is passed to **GPT-Neo** for generating a response.

3. **Deployment**:
   - The pipeline is served using FastAPI and containerized with Docker.
   - Milvus, MinIO, and other dependencies are orchestrated using Docker Compose.

---

## Features

- **Vector Database**: Uses Milvus for efficient storage and retrieval of embeddings.
- **Embedding Model**: Leverages `sentence-transformers/all-MiniLM-L6-v2` for embedding generation.
- **Language Model**: Uses GPT-Neo (EleutherAI/gpt-neo-1.3B) for text generation.
- **Web API**: FastAPI endpoints for document upload and query handling.
- **Scalable Deployment**: Containerized pipeline with Docker and Docker Compose.

---

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Database**: Milvus
- **Language Model**: `EleutherAI/gpt-neo-1.3B`
- **Document Preprocessing**: PyPDF2
- **Containerization**: Docker and Docker Compose

---

## Setup Instructions

### Prerequisites

- Python 3.9 or later
- Docker and Docker Compose installed
- GPU (optional but recommended for faster inference)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/rag-pipeline.git
cd rag-pipeline
```

