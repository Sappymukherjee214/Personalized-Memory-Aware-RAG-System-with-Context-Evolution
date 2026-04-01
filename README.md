# Personalized Memory-Aware RAG with Cognitive Context Evolution (C-RAG)

## *A Comprehensive Framework for Longitudinal Intent Trajectory Modeling and Cognitive Disentanglement*

[![Python](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com)
[![Frontend](https://img.shields.io/badge/Interface-Glassmorphism-blue)](https://github.com/Sappymukherjee214/Personalized-Memory-Aware-RAG-System-with-Context-Evolution)
[![Datasets](https://img.shields.io/badge/Benchmarking-Kaggle-orange)](#dataset-integration)
[![Metrics](https://img.shields.io/badge/Evaluation-NDCG--REI-red)](#evaluation-methodology)

---

## 🔬 1. Project Overview & Research Context

Traditional Retrieval-Augmented Generation (RAG) architectures operate under the **Stateless Assumption**. Every query is processed as an isolated, independent and identically distributed (i.i.d.) event. While this is efficient for generic Q&A, it fails in **high-stakes research environments** where a user’s knowledge base evolves over time.

**C-RAG** (Cognitive-RAG) rejects the stateless paradigm. Instead, it proposes a system that models the user’s **Intent Trajectory**. By treating every interaction as a node in a evolving semantic graph, C-RAG achieves a level of personalization that mirrors the human executive function.

---

## 🏛️ 2. The Cognitive Disentanglement Architecture

The system is built on a tripartite cognitive model, separating raw data from extracted knowledge.

### 2.1 Episodic Short-Term Memory (STM)

The STM serves as the high-fidelity input buffer. Unlike standard chat history, the STM in C-RAG is **Weighted by Salience**.

- **Sliding Window**: Consists of the last $N$ interactions (default $N=5$).
- **Salience Scoring**: Each item is assigned a confidence score based on the **Research Efficiency Index (REI)** at the time of its creation.

### 2.2 Semantic Long-Term Memory (LTM)

The LTM is the "Axiom Registry." It does not store raw chat; it stores **Distilled Research Axioms**. When the STM reaches its limit, the system undergoes a **Consolidation Cycle**.

- **Knowledge Distillation**: The most relevant item is summarized into a foundational axiom.
- **Durable Persistence**: All LTM items are synced to a production-grade JSON layer for multi-session stability.

### 2.3 Information Bottleneck Analysis (IBA)

During the transition from STM to LTM, the system applies **IBA Distillation**. The goal is to maximize **Semantic Retainment** while minimizing **Token Complexity**.

- **Calculus**: $IBA = 1 - \frac{T_{final}}{T_{initial}}$ where $T$ represents the token count.

---

## 🎨 3. Technical Illustrations (System in Action)

### Dashboard Architecture

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

## 📊 4. Dataset Integration & Methodology

### 4.1 DailyDialog Integration

The **DailyDialog** dataset is utilized for modeling **Natural Conversational Intent**.

- **Rationale**: Research interactions are rarely one-off. DailyDialog provides multi-turn trajectories that allow us to test if the system can follow shift in logic.

### 4.2 PersonaChat Integration

The **PersonaChat** dataset is utilized for **Semantic Identity Verification**.

- **Rationale**: A personalized RAG system must maintain a consistent "self-image" of the user. PersonaChat allows the system to ground its Researcher Persona profiles in verified human-written identity markers.

---

## 🔥 5. Experimental Evaluation (AQE Suite)

C-RAG includes a built-in **Automated Quantitative Evaluation (AQE)** engine.

### 5.1 NDCG (Normalized Discounted Cumulative Gain)

We use NDCG at $k=5$ to measure the quality of the personalized retrieval.

- **Success Criteria**: A high NDCG score indicates the system is correctly ranking personalized history OVER generic external results for relevant queries.

### 5.2 Hallucination Probability Index

The system calculates a "Hallucination Gradient" based on token overlap with verified grounding data.

- **Formula**: $H = 1.0 - \frac{Matches(Response, context)}{TotalTokens(Response)}$

---

## 🛠️ 6. Core Module Breakdown

- **`memory_engine.py`**: The heart of the system. Implements the `UltimateMemoryEngine` class.
- **`rag_pipeline.py`**: Orchestrates the dual-retrieval track (Internal Personal vs. External Research).
- **`data_loader.py`**: Handles asynchronous downloading of Kaggle research datasets.
- **`eval_engine.py`**: The laboratory module. Calculates the NDCG and Hallucination metrics.
- **`main.py`**: The API Gateway and static dashboard host.

---

## 📡 7. Full API Reference

### Cognitive Endpoints

- `GET /memory/state`: Returns the full JSON representation of the STM and LTM tracks.
- `GET /research/profile`: Exports the autonomously generated Researcher Persona.

### Laboratory Endpoints

- `GET /research/simulation`: Runs a 5-turn research simulation on the DailyDialog dataset.
- `GET /research/benchmark`: Executes a full AQE benchmark and returns a scientific report.
- `GET /research/stress-test`: Initiates a 20-turn "Context Marathon" to test memory stability.

---

## 🚀 8. Future Research Roadmap

### Phase 5: Relational Knowledge Graphs

Migration of the Semantic LTM from a JSON flat-store to a **Neo4j Graph Database** to enable multi-hop reasoning.

### Phase 6: Active Forgetting Loops

Introduction of a **Saliency Decay Algorithm** that autonomously "forgets" low-utility data points.

### Phase 7: Collaborative Memory

Implementing a privacy-preserved **Federated Memory Layer** where multiple C-RAG instances can share insights.

---

## 📜 9. License & Professional Contact

This project is released under the **MIT License**. It is designed for researchers at **IITs, NITs, IISERs, and global R&D institutions.**

**Author**: Sappymukherjee214

**Research Focus**: Agentic Memory Architectures and Cognitive Context Evolution.

---

Built for the next generation of personalized knowledge synthesis. 🚀
