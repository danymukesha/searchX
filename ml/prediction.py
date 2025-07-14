import torch
from transformers import AutoModel, AutoTokenizer

class ProteinFunctionPredictor:
    def __init__(self):
        self.model = AutoModel.from_pretrained("facebook/esm2_t33_650M_UR50D")
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/esm2_t33_650M_UR50D")

    def predict(self, sequence: str) -> Dict:
        inputs = self.tokenizer(sequence, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)
        return {"embedding": embeddings.numpy().tolist()}
