from fastapi import FastAPI
from core.search import ContextAwareSearcher
from core.database import DatabaseManager

app = FastAPI()
db_manager = DatabaseManager()
searcher = ContextAwareSearcher(db_manager)

@app.get("/search")
async def search(query: str, context: str = "general"):
    return searcher.search(query, {"mode": context})

@app.post("/predict")
async def predict_function(sequence: str):
    predictor = ProteinFunctionPredictor()
    return predictor.predict(sequence)
