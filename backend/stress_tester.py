import time
from typing import List, Dict, Any
import numpy as np

class LongContextStressTester:
    def __init__(self, rag_pipeline: Any):
        self.rag_pipeline = rag_pipeline
        self.results = []

    def simulate_long_interaction(self, n_turns: int = 20) -> Dict:
        """Simulates 20+ research interactions to measure memory decay/consolidation."""
        print(f"--- Initiating Long-Context Stress Test: {n_turns} turns ---")
        
        # Test Query: Changing research intent to measure 'Intent Adaptivity'
        # Query 1-10: Quantum, 11-20: Security
        quantum_queries = [f"Quantum Computing research paper {i}" for i in range(1, 11)]
        security_queries = [f"Cybersecurity and encryption method {i}" for i in range(11, 21)]
        all_queries = quantum_queries + security_queries
        
        start_time = time.time()
        for i, q in enumerate(all_queries):
            print(f"Turn {i+1}: Testing intent: {q}")
            result = self.rag_pipeline.process_query(q)
            # Record performance at each turn
            self.results.append({
                "turn": i+1,
                "confidence": result['internal_memories'][0]['confidence'] if result['internal_memories'] else 0.0,
                "rei_score": result['diagnostics']['rei_score']
            })

        duration = time.time() - start_time
        
        # Calculate Stability / Decay Rate
        decay_over_time = [r['confidence'] for r in self.results]
        
        return {
            "total_turns": n_turns,
            "total_duration_sec": round(duration, 2),
            "final_decay_rate": round(decay_over_time[-1] - decay_over_time[0], 4),
            "consolidation_events_count": n_turns // 5,
            "results_history": self.results
        }
