from sck_runtime.skills.base import Skill
from sck_runtime.truth.classifier import classify_claim


def activation(state):
    return True


def execute(state):
    claim = state.input
    result = classify_claim(claim)

    state.truth_registry["root"] = result
    return state


skill = Skill(
    id="spectral_truth_alignment",
    priority=1,
    activation_conditions=activation,
    execution_fn=execute,
    dependencies=[]
)
