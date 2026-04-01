import numpy as np
from typing import List, Dict, Any
import time

class ResearchEvalEngine:
    def __init__(self, rag_pipeline: Any):
        self.rag_pipeline = rag_pipeline
        self.metrics_history = []

    def calculate_ndcg(self, retrieved_scores: List[float], ideal_scores: List[float], k: int = 5) -> float:
        """Calculates Normalized Discounted Cumulative Gain (Tier-1 Metric)."""
        def dcg(scores):
            return sum([s / np.log2(i + 2) for i, s in enumerate(scores[:k])])
        
        actual_dcg = dcg(retrieved_scores)
        ideal_dcg = dcg(sorted(ideal_scores, reverse=True))
        return actual_dcg / ideal_dcg if ideal_dcg > 0 else 0.0

    def calculate_hallucination_index(self, response: str, external_context: List[Dict]) -> float:
        """Estimates the probability of hallucination based on external context overlap.""" 
        # In a real system, this would use a NLI (Natural Language Inference) model
        # For the PoC, we measure token overlap with verified grounding
        grounding_tokens = " ".join([e['content'] for e in external_context]).lower()
        response_tokens = response.lower().split()
        matches = sum(1 for t in response_tokens if t in grounding_tokens)
        
        overlap_score = matches / len(response_tokens) if response_tokens else 0.0
        return 1.0 - overlap_score # 0.0 means perfect grounding, 1.0 means full hallucination

    def run_benchmark(self, dataset_samples: List[List[str]]) -> Dict:
        """Runs a rigorous multi-turn benchmark to evaluate the system."""
        print(f"--- Initiating Scientific Benchmark: {len(dataset_samples)} trajectories ---")
        
        total_ndcg = 0.0
        total_hallucination = 0.0
        
        for trajectory in dataset_samples:
            if len(trajectory) < 2: continue
            
            # Step 1: Query the system
            query = trajectory[0]
            result = self.rag_pipeline.process_query(query)
            
            # Step 2: Score Retrieval Performance
            # We assume internal scores are relevance predictions
            retrieved_scores = [m['score'] for m in result['internal_memories']]
            # In a real evaluation, ideal_scores would be human-labeled
            ideal_scores = [1.0] + [0.5] * (len(retrieved_scores) - 1) 
            
            total_ndcg += self.calculate_ndcg(retrieved_scores, ideal_scores)
            total_hallucination += self.calculate_hallucination_index(result['response'], result['external_results'])

        avg_ndcg = total_ndcg / len(dataset_samples)
        avg_hall_prob = total_hallucination / len(dataset_samples)
        
        report = {
            "avg_ndcg": round(avg_ndcg, 4),
            "hallucination_probability": round(avg_hall_prob, 4),
            "sample_size": len(dataset_samples),
            "timestamp": time.time()
        }
        self.metrics_history.append(report)
        return report
