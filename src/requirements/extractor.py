"""
Step 2 — JD requirement extractor.

Responsibilities:
  - Accept raw JD text.
  - Call the LLM (cached) to extract atomic requirements.
  - Validate output against a Pydantic schema.
  - Return a list of Requirement objects tagged required/preferred.

Libraries: openai, pydantic, diskcache.
"""

# TODO: define Requirement(BaseModel) with fields: text, kind (required|preferred)
# TODO: implement extract_requirements(jd_text: str) -> list[Requirement]
