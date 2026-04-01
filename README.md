# Personalized Memory-Aware RAG with Cognitive Context Evolution (C-RAG)

## *A Comprehensive Framework for Longitudinal Intent Trajectory Modeling and Cognitive Disentanglement*

[![Python](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com)
[![Frontend](https://img.shields.io/badge/Interface-Glassmorphism-blue)](https://github.com/Sappymukherjee214/Personalized-Memory-Aware-RAG-System-with-Context-Evolution)
[![Datasets](https://img.shields.io/badge/Benchmarking-Kaggle-orange)](#dataset-integration)
[![Metrics](https://img.shields.io/badge/Evaluation-NDCG--REI-red)](#evaluation-methodology)

---

## Project Overview

Traditional Retrieval-Augmented Generation (RAG) architectures operate under the **Stateless Assumption**. Every query is processed as an isolated, independent and identically distributed (i.i.d.) event. While this is efficient for generic Q&A, it fails in **high-stakes research environments** where a user’s knowledge base evolves over time.

**C-RAG** (Cognitive-RAG) rejects the stateless paradigm. Instead, it proposes a system that models the user’s **Intent Trajectory**. By treating every interaction as a node in a evolving semantic graph, C-RAG achieves a level of personalization that mirrors the human executive function.

---

## Cognitive Disentanglement Architecture

The system is built on a tripartite cognitive model, separating raw data from extracted knowledge.

### Episodic Short-Term Memory (STM)

The STM serves as the high-fidelity input buffer. Unlike standard chat history, the STM in C-RAG is **Weighted by Salience**.

- **Sliding Window**: Consists of the last $N$ interactions (default $N=5$).
- **Salience Scoring**: Each item is assigned a confidence score based on the **Research Efficiency Index (REI)** at the time of its creation.

### Semantic Long-Term Memory (LTM)

The LTM is the "Axiom Registry." It does not store raw chat; it stores **Distilled Research Axioms**. When the STM reaches its limit, the system undergoes a **Consolidation Cycle**.

- **Knowledge Distillation**: The most relevant item is summarized into a foundational axiom.
- **Durable Persistence**: All LTM items are synced to a production-grade JSON layer for multi-session stability.

### Information Bottleneck Analysis (IBA)

During the transition from STM to LTM, the system applies **IBA Distillation**. The goal is to maximize **Semantic Retainment** while minimizing **Token Complexity**.

- **Calculus**: $IBA = 1 - \frac{T_{final}}{T_{initial}}$ where $T$ represents the token count.

---

## Technical Illustrations (Live Workspace Capture)

### Ultimate Research Dashboard

The **C-RAG Evolution Dashboard** featuring Vanguard Glass-CSS and real-time intent visualization.

![Ultimate Research Interface](assets/dashboard_full.png)

### Cognitive Memory Evolution

Visualization of the **STM-to-LTM** transition (Episodic to Semantic) and **IBA Compression** Efficiency.

![Memory Evolution & Consolidation](assets/memory_evolution.png)

### Scientific Laboratory (AQE)

Real-time **NDCG** and **Hallucination Probability** reports from a 10-trajectory DailyDialog simulation.

![Scientific Evaluation Rigor](assets/benchmark_report.png)

### Autonomous Researcher Persona

Expertise discovery and identity export based on longitudinal interaction history.

![Semantic Identity Profiling](assets/persona_profile.png)

---

## Dataset Integration

The **DailyDialog** dataset is utilized for modeling **Natural Conversational Intent**. Research interactions are rarely one-off. DailyDialog provides multi-turn trajectories that allow us to test if the system can follow shift in logic.

The **PersonaChat** dataset is utilized for **Semantic Identity Verification**. A personalized RAG system must maintain a consistent "self-image" of the user. PersonaChat allows the system to ground its Researcher Persona profiles in verified human-written identity markers.

---

## Evaluation Methodology

This project includes a dedicated **AQE (Automated Quantitative Evaluation)** Suite:

| Metric | Scientific Importance | Description |
| :--- | :--- | :--- |
| **NDCG** | Retrieval Precision | Measures how effectively the system ranks internal history over noise. |
| **Hallucination Index** | Factuality | Based on contradiction with Long-Term Memory grounding. |
| **AMW Stability** | Adaptive Weighting | Adjusts retrieval math based on historical REI success. |

---

## Core Module Breakdown

- **`memory_engine.py`**: The heart of the system. Implements the `UltimateMemoryEngine` class.
- **`rag_pipeline.py`**: Orchestrates the dual-retrieval track (Internal Personal vs. External Research).
- **`data_loader.py`**: Handles asynchronous downloading of Kaggle research datasets.
- **`eval_engine.py`**: The laboratory module. Calculates the NDCG and Hallucination metrics.
- **`main.py`**: The API Gateway and static dashboard host.

---

## How to Run

1. **Backend**: `python backend/main.py`.
2. **Frontend**: Open `frontend/index.html`.
3. **Simulation**: Click **"Run AQE Benchmark"** in the sidebar.

---

## Future Research Roadmap

### Phase 5: Relational Knowledge Graphs

Migration of the Semantic LTM from a JSON flat-store to a **Neo4j Graph Database** to enable multi-hop reasoning.

### Phase 6: Active Forgetting Loops

Introduction of a **Saliency Decay Algorithm** that autonomously "forgets" low-utility data points.

### Phase 7: Collaborative Memory

Implementing a privacy-preserved **Federated Memory Layer** where multiple C-RAG instances can share insights.

---

## License & Professional Contact

This project is released under the **MIT License**. It is designed for researchers at **IITs, NITs, IISERs, and global R&D institutions.**

**Author**: Sappymukherjee214

**Research Focus**: Agentic Memory Architectures and Cognitive Context Evolution.

---

Built for the next generation of personalized knowledge synthesis. 🚀
