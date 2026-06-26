from dataclasses import dataclass
from typing import Callable, Any
from sck_runtime.kernel.state import KernelState


@dataclass
class Skill:
    id: str
    priority: int

    activation_conditions: Callable[[KernelState], bool]
    execution_fn: Callable[[KernelState], KernelState]

    dependencies: list[str] = None

    conflict_policy: str = "PIPELINE"
