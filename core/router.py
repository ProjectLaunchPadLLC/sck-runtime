from sck_runtime.skills.registry import get_all_skills


def activate_skills(state):
    active = []

    for skill in get_all_skills():
        if skill.activation_conditions(state):
            active.append(skill)

    return sorted(active, key=lambda s: s.priority)
