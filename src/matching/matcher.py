"""
Step 3 — Semantic matcher.

Responsibilities:
  - Embed resume lines and JD requirements using sentence-transformers.
  - Build a FAISS index over resume line embeddings.
  - For each requirement, retrieve top-K nearest resume lines.

Libraries: sentence-transformers, faiss-cpu.
Config: embedding_model, faiss_top_k from config/weights.yaml.
"""

# TODO: implement build_index(lines: list[str]) -> FAISSIndex
# TODO: implement match(requirement_text: str, index: FAISSIndex) -> list[tuple[str, float]]
