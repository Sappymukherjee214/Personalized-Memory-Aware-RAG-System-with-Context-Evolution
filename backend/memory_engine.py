import time
import json
import os
from typing import List, Dict, Optional, Any, Set
import numpy as np

class MemoryItem:
    def __init__(self, content: str, embedding: np.ndarray, metadata: Dict[str, Any]):
        self.content = content
        self.embedding = embedding
        self.metadata = metadata
        self.timestamp = metadata.get("timestamp", time.time())
        self.access_count = metadata.get("access_count", 0)
        self.salience = metadata.get("salience", 0.7)
        self.confidence = metadata.get("confidence", 1.0)
        self.entities: Set[str] = set(metadata.get("entities", []))

    def to_dict(self) -> Dict:
        return {
            "content": self.content,
            "embedding": self.embedding.tolist() if isinstance(self.embedding, np.ndarray) else self.embedding,
            "metadata": {
                **self.metadata,
                "timestamp": self.timestamp,
                "access_count": self.access_count,
                "salience": self.salience,
                "confidence": self.confidence,
                "entities": list(self.entities)
            }
        }

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(data["content"], np.array(data["embedding"]), data["metadata"])

class UltimateMemoryEngine:
    def __init__(self, stm_limit: int = 5, persist_path: str = "ultimate_memory.json"):
        self.episodic_stm: List[MemoryItem] = []  
        self.semantic_ltm: List[MemoryItem] = []  
        self.stm_limit = stm_limit
        self.persist_path = persist_path
        self.context_embedding: Optional[np.ndarray] = None
        self.weights = {"sim": 0.5, "alignment": 0.3, "confidence": 0.2}
        self.efficiency_history = []
        self.last_compression_ratio = 0.0
        
        # Initial Load from Disk
        self.load_from_disk()

    def _extract_entities(self, text: str) -> List[str]:
        keywords = ["quantum", "ai", "security", "encryption", "ethics", "paper", "research"]
        return [k for k in keywords if k in text.lower()]

    def save_to_disk(self):
        """Production Serializer: Saves knowledge to JSON."""
        state = {
            "stm": [m.to_dict() for m in self.episodic_stm],
            "ltm": [m.to_dict() for m in self.semantic_ltm],
            "weights": self.weights,
            "efficiency_history": self.efficiency_history,
            "last_compression_ratio": self.last_compression_ratio
        }
        with open(self.persist_path, 'w') as f:
            json.dump(state, f, indent=2)

    def load_from_disk(self):
        """Production Hydrator: Loads knowledge from JSON."""
        if not os.path.exists(self.persist_path): return
        try:
            with open(self.persist_path, 'r') as f:
                state = json.load(f)
                self.episodic_stm = [MemoryItem.from_dict(m) for m in state.get("stm", [])]
                self.semantic_ltm = [MemoryItem.from_dict(m) for m in state.get("ltm", [])]
                self.weights = state.get("weights", self.weights)
                self.efficiency_history = state.get("efficiency_history", [])
                self.last_compression_ratio = state.get("last_compression_ratio", 0.0)
            print(f"--- Global Researcher Memory Hydrated: {len(self.semantic_ltm)} Axioms Loaded ---")
        except Exception as e:
            print(f"Persistence Warning: {e}")

    def update_retrieval_weights(self, rei_score: float):
        self.efficiency_history.append(rei_score)
        if len(self.efficiency_history) > 5:
            avg_rei = sum(self.efficiency_history[-5:]) / 5
            if avg_rei > 0.8:
                self.weights["alignment"] += 0.05
                self.weights["sim"] -= 0.05
            elif avg_rei < 0.5:
                self.weights["sim"] += 0.05
                self.weights["alignment"] -= 0.05
        
        total = sum(self.weights.values())
        self.weights = {k: v/total for k, v in self.weights.items()}

    def consolidate_memories(self):
        if not self.episodic_stm: return
        initial_tokens = sum(len(m.content.split()) for m in self.episodic_stm)
        high_salience = [m for m in self.episodic_stm if m.salience > 0.5]
        
        if high_salience:
            summary = high_salience[0]
            summary.content = f"[Ultimate Axiom]: {summary.content.split('->')[0].replace('User: ', '')}"
            summary.metadata['type'] = 'semantic'
            self.semantic_ltm.append(summary)
            self.last_compression_ratio = 1.0 - (len(summary.content.split()) / initial_tokens)
            
        self.episodic_stm = []
        self.save_to_disk() # Sync to disk after consolidation

    def add_interaction(self, query: str, response: str, embedding: np.ndarray):
        entities = self._extract_entities(query)
        item = MemoryItem(f"User: {query} -> Bot: {response}", embedding, 
                          {"type": "episodic", "salience": 0.8, "entities": entities})
        self.episodic_stm.append(item)

        if len(self.episodic_stm) >= self.stm_limit:
            self.consolidate_memories()
        
        self.save_to_disk() # Persistent Sync

    def retrieve(self, query_embedding: np.ndarray, top_k: int = 4) -> List[Dict]:
        all_items = self.episodic_stm + self.semantic_ltm
        scored_results = []

        for item in all_items:
            sim = np.dot(query_embedding.flatten(), item.embedding.flatten()) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(item.embedding)
            )
            
            alignment = 0.0
            if self.context_embedding is not None:
                alignment = np.dot(self.context_embedding.flatten(), item.embedding.flatten()) / (
                    np.linalg.norm(self.context_embedding) * np.linalg.norm(item.embedding)
                )

            final_score = (sim * self.weights["sim"]) + (alignment * self.weights["alignment"]) + (item.confidence * self.weights["confidence"])
            
            scored_results.append({
                "content": item.content,
                "score": round(float(final_score), 4),
                "confidence": round(float(item.confidence), 4),
                "type": item.metadata['type']
            })

        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:top_k]

    def get_ultimate_metrics(self) -> Dict:
        return {
            "compression_efficiency_iba": round(self.last_compression_ratio, 4),
            "adaptive_weights": {k: round(v, 2) for k, v in self.weights.items()},
            "rei_avg": round(sum(self.efficiency_history) / max(1, len(self.efficiency_history)), 3)
        }
    
    def generate_researcher_profile(self) -> Dict:
        topics = {}
        for m in self.semantic_ltm:
            for e in m.entities:
                topics[e] = topics.get(e, 0) + 1
        
        return {
            "primary_expertise": max(topics, key=topics.get) if topics else "Universal Researcher",
            "knowledge_depth": len(self.semantic_ltm),
            "research_style": "Adaptive - Non Linear" if self.weights["alignment"] > 0.4 else "Foundational - Linear",
            "top_topics": sorted(topics.items(), key=lambda x: x[1], reverse=True)[:3]
        }
