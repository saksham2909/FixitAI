"""
Step 5 — Requirement scorer.

Responsibilities:
  - Compute per-requirement score Si using:
      Si = w_match * match_score
         + w_evidence * evidence_score
         + w_context * context_score
         + w_importance * importance_score
  - Aggregate Si values into an overall resume–JD compatibility score.
  - Load weights from config/weights.yaml.

Libraries: pyyaml, numpy.
"""

# TODO: implement score_requirement(match, evidence, context, importance, weights) -> float
# TODO: implement overall_score(requirement_scores: list[float]) -> float
