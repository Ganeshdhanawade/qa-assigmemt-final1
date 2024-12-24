from transformers import AutoTokenizer, AutoModelForCausalLM

class QueryModel:
    def __init__(self):
        #initiate the llma model and tokenizer
        self.model_name = "meta-llama/Llama-2-7b-hf"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def answer_query(self, query, chunks):
        """ answer quary based on top chunk using LLaMA model."""
        best_answer = None
        for chunk in chunk:
            ##prepare the prompt of for answering the quations
            prompt = f"Given the following context, answer the queation. \n\nContext: {chunk} \n\nQuestion: {query}\nAnswer:"

            #tokenize the input and generate aresponce using LLaMA
            inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True,padding=True)
            outputs = self.model.generate(inputs['input_ids'],max_length = 512, num_return_sequences=1)
            answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

            #extract the answer text
            answer_text = answer.split("Answer:")[-1].strip()
            if not best_answer or answer_text:
                best_answer = answer_text
        return best_answer if best_answer else "I don't know" 