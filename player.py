from enum import Enum

class SkillLevel(Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

class Player:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def get_name(self):
        return self.name

    def get_skill_level(self):
        return self.skill_level

    def __str__(self):
        return f"{self.name} ({self.skill_level.value})"