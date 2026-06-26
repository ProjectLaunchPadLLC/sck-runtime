from sck_runtime.kernel.state import KernelState
from sck_runtime.core.router import activate_skills
from sck_runtime.kernel.dag import build_dag
from sck_runtime.kernel.executor import execute_dag
from sck_runtime.truth.spectral import spectral_truth_filter


def run_kernel(input_text: str) -> KernelState:
    state = KernelState(input=input_text)

    # 1. Skill activation
    skills = activate_skills(state)
    state.active_skills = skills

    # 2. DAG construction
    dag = build_dag(skills)
    state.execution_graph = dag

    # 3. Execution
    state = execute_dag(state, dag)

    # 4. Truth filtering
    state = spectral_truth_filter(state)

    return state
