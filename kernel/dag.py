from collections import defaultdict

class DAG:
    def __init__(self):
        self.edges = defaultdict(list)


def build_dag(skills):
    dag = DAG()

    skill_map = {s.id: s for s in skills}

    for skill in skills:
        deps = skill.dependencies or []
        for dep in deps:
            dag.edges[dep].append(skill.id)

    return dag
