def execute_dag(state, dag):

    executed = set()

    def execute(skill_id):
        if skill_id in executed:
            return

        # execute dependencies first
        for child in dag.edges.get(skill_id, []):
            execute(child)

        skill = state.active_skills_map[skill_id]
        state = skill.execution_fn(state)

        state.intermediate_results[skill_id] = state
        executed.add(skill_id)

    for skill in state.active_skills:
        execute(skill.id)

    return state
