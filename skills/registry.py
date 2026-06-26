from typing import Dict
from sck_runtime.skills.base import Skill


SKILL_REGISTRY: Dict[str, Skill] = {}


def register_skill(skill: Skill):
    SKILL_REGISTRY[skill.id] = skill


def get_all_skills():
    return list(SKILL_REGISTRY.values())
