from enum import Enum


class TruthClass(str, Enum):
    T0 = "T0"
    T0_5 = "T0.5"
    T1 = "T1"
    T1_5 = "T1.5"
    T2 = "T2"
    T2_5 = "T2.5"
    T3 = "T3"


def spectral_truth_filter(state):
    filtered = {}

    for k, claim in state.truth_registry.items():
        if claim["classification"] == TruthClass.T3:
            continue
        filtered[k] = claim

    state.truth_registry = filtered
    return state
