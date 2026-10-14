"""
Baselines — Five reference scorers for benchmarking.

  1. keyword_overlap   — Jaccard / token overlap between JD and resume.
  2. tfidf_cosine      — TF-IDF vectorisation + cosine similarity.
  3. embedding_cosine  — Sentence-transformer embeddings, no FAISS index.
  4. llm_direct        — Prompt LLM to output a compatibility score directly (cached).
  5. fixitai_pipeline  — Full FixitAI pipeline score (imported from src/).
"""

# TODO: implement each baseline as a function:
#   score(resume_text: str, jd_text: str) -> float  (0–1)
