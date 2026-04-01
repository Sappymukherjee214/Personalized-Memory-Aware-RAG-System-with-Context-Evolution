from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from typing import List, Dict, Any, Optional
import pydantic
from backend.memory_engine import UltimateMemoryEngine
from backend.rag_pipeline import EliteRAGPipeline
from backend.data_loader import ResearchDataLoader
from backend.eval_engine import ResearchEvalEngine
from backend.stress_tester import LongContextStressTester
import traceback

app = FastAPI(title="Ultimate Personalized Memory-Aware RAG API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Elite Research Modules
memory_engine = UltimateMemoryEngine()
rag_pipeline = EliteRAGPipeline(memory_engine)
data_loader = ResearchDataLoader()
eval_engine = ResearchEvalEngine(rag_pipeline)
stress_tester = LongContextStressTester(rag_pipeline)

# Mount Frontend
app.mount("/view", StaticFiles(directory="frontend", html=True), name="static")

class QueryRequest(pydantic.BaseModel):
    query: str

class QueryResponse(pydantic.BaseModel):
    query: str
    response: str
    internal_memories: List[Dict[str, Any]]
    external_results: List[Dict[str, Any]]
    diagnostics: Dict[str, Any] # This must match rag_pipeline.py

@app.get("/")
def read_root():
    return {"message": "System Online", "ultimate_metrics": memory_engine.get_ultimate_metrics()}

@app.post("/query", response_model=QueryResponse)
def process_query(request: QueryRequest):
    try:
        result = rag_pipeline.process_query(request.query)
        # Ensure result has the expected keys
        if "diagnostics" not in result and "context_state" in result:
             result["diagnostics"] = result.pop("context_state")
        
        return QueryResponse(**result)
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/state")
def get_memory_state():
    """Returns detailed state of Episodic STM and Semantic LTM with Ultimate Diagnostics."""
    return {
        "stm": [{"content": m.content, "timestamp": m.timestamp, "type": m.metadata["type"]} for m in memory_engine.episodic_stm],
        "ltm": [{"content": m.content, "timestamp": m.timestamp, "type": m.metadata["type"]} for m in memory_engine.semantic_ltm],
        "ultimate_metrics": memory_engine.get_ultimate_metrics()
    }

@app.get("/research/profile")
def get_researcher_profile():
    return memory_engine.generate_researcher_profile()

@app.get("/research/simulation")
def run_simulation(limit: int = 5):
    try:
        conversations = data_loader.load_daily_dialog(limit)
        results = []
        for conv in conversations:
            if len(conv) >= 2:
                results.append(rag_pipeline.process_query(conv[0]))
        return {"simulation_results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Simulation error: {str(e)}")

@app.get("/research/benchmark")
def run_benchmark(limit: int = 10):
    report = eval_engine.run_benchmark(data_loader.load_daily_dialog(limit))
    return {"report": report}

@app.get("/research/stress-test")
def run_stress_test(turns: int = 20):
    report = stress_tester.simulate_long_interaction(turns)
    return {"stress_test_results": report}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
