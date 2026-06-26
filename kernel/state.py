from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class KernelState:
    input: str

    intent_vector: List[float] = field(default_factory=list)
    emotion_vector: List[float] = field(default_factory=list)

    epistemic_context: Dict[str, Any] = field(default_factory=dict)

    active_skills: List[str] = field(default_factory=list)

    execution_graph: Any = None
    intermediate_results: Dict[str, Any] = field(default_factory=dict)

    truth_registry: Dict[str, Any] = field(default_factory=dict)

    final_output: str = ""
