# Personalized Memory-Aware RAG with Context Evolution

This project implements a research-oriented Retrieval-Augmented Generation (RAG) system that moves beyond stateless interactions by incorporating tiered memory (STM/LTM) and dynamic context evolution.

## 🚀 Research Vision

The core objective is to model the **Intent Trajectory** of a user. Instead of treating each query in isolation, the system maintains a **Dynamic Context Embedding (DCE)** that evolves with every interaction, allowing the generator to "recall" past preferences and "anticipate" future research directions.

## 🏗️ Architecture

- **Short-Term Memory (STM):** A high-fidelity sliding window of recent interactions (5 turns).
- **Long-Term Memory (LTM):** Consolidated knowledge filtered via a decay function $W(t) = e^{-\lambda t}$.
- **Context Evolution:** A weighted Exponential Moving Average (EMA) of query embeddings that shifts the system's "focus" based on semantic drift.
- **Dual Retrieval:** Queries search across both a global knowledge base (External) and personal history (Internal).

## 📊 Dataset Integration

The system is integrated with the following research datasets via `kagglehub`:

- **DailyDialog**: Used for modeling natural conversational flow and intent transitions.
- **PersonaChat**: Used for testing the consistency of personalized memory over multi-session interactions.

## 🏗️ Components

- `backend/memory_engine.py`: Core logic for memory formation and DCE updating.
- `backend/rag_pipeline.py`: Orchestrates dual-retrieval and grounding evidence.
- `backend/data_loader.py`: Handles Kaggle dataset downloads and pre-processing.
- `backend/main.py`: FastAPI server for communication and simulation.
- `frontend/`: A premium, dark-mode research dashboard using vanilla CSS and JS.

## 🏁 How to Run

1. **Backend:**

   ```bash
   pip install -r requirements.txt
   python backend/main.py
   ```

2. **Frontend:**
   Open `frontend/index.html` in any modern browser.

3. **Run Simulation:**
   Visit `http://localhost:8000/research/simulation?limit=5` to trigger a research simulation using the DailyDialog dataset.

## 🧪 Evaluation Metrics (Proposed)

- **NDCG@k:** Accuracy of personalized retrieval vs. baseline RAG.
- **Context Alignment Score:** Cosine similarity between response and latent intent trajectory.
- **Hallucination Rate:** Measured by contradiction with LTM grounding.

---
*Created as part of the Advanced Agentic Coding Research Proposal.*
