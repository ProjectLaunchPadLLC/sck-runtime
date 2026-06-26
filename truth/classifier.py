def classify_claim(claim: str):
    return {
        "claim": claim,
        "classification": "T1.5",
        "grounding_depth": 1,
        "spectral_score": 0.5
    }
