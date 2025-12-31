import random
from player import Player, SkillLevel
from team import Team

class Group:
    def __init__(self, group_number, is_forced=False):
        self.group_number = group_number
        self.players = []
        self.is_forced = is_forced
        self.team1 = None
        self.team2 = None

    def is_forced(self):
        return self.is_forced

    def set_forced(self, forced):
        self.is_forced = forced

    def add_player(self, player):
        if len(self.players) >= 4:
            raise ValueError("Group is full (4 players maximum)")
        self.players.append(player)

    def get_players(self):
        return self.players.copy()

    def get_group_number(self):
        return self.group_number

    def is_full(self):
        return len(self.players) == 4

    def get_team1(self):
        return self.team1

    def get_team2(self):
        return self.team2

    def split_into_teams(self):
        if len(self.players) != 4:
            return  # Can only split groups of 4

        # Count players by skill level
        beginners = [p for p in self.players if p.get_skill_level() == SkillLevel.BEGINNER]
        intermediates = [p for p in self.players if p.get_skill_level() == SkillLevel.INTERMEDIATE]
        advanced = [p for p in self.players if p.get_skill_level() == SkillLevel.ADVANCED]

        # Shuffle for randomization
        random.shuffle(beginners)
        random.shuffle(intermediates)
        random.shuffle(advanced)

        self.team1 = Team("Team 1")
        self.team2 = Team("Team 2")

        # Condition 1: All intermediate (4I)
        if len(beginners) == 0 and len(advanced) == 0 and len(intermediates) == 4:
            self.team1.add_player(intermediates[0])
            self.team1.add_player(intermediates[1])
            self.team2.add_player(intermediates[2])
            self.team2.add_player(intermediates[3])
        # Condition 2: All advanced (4A)
        elif len(beginners) == 0 and len(intermediates) == 0 and len(advanced) == 4:
            self.team1.add_player(advanced[0])
            self.team1.add_player(advanced[1])
            self.team2.add_player(advanced[2])
            self.team2.add_player(advanced[3])
        # Condition 3: Advanced with Beginner vs two intermediate (1A + 1B vs 2I)
        elif len(advanced) == 1 and len(beginners) == 1 and len(intermediates) == 2:
            self.team1.add_player(advanced[0])
            self.team1.add_player(beginners[0])
            self.team2.add_player(intermediates[0])
            self.team2.add_player(intermediates[1])
        # Condition 4: Advanced with beginner vs advanced with beginner (2A + 2B)
        elif len(advanced) == 2 and len(beginners) == 2 and len(intermediates) == 0:
            self.team1.add_player(advanced[0])
            self.team1.add_player(beginners[0])
            self.team2.add_player(advanced[1])
            self.team2.add_player(beginners[1])
        # Condition 5: Advanced with intermediate vs Advanced with intermediate (2A + 2I)
        elif len(advanced) == 2 and len(intermediates) == 2 and len(beginners) == 0:
            self.team1.add_player(advanced[0])
            self.team1.add_player(intermediates[0])
            self.team2.add_player(advanced[1])
            self.team2.add_player(intermediates[1])
        # Other combinations - try to balance as best as possible
        else:
            # Default: try to balance skill levels
            all_players = self.players.copy()
            random.shuffle(all_players)

            self.team1.add_player(all_players[0])
            self.team1.add_player(all_players[1])
            self.team2.add_player(all_players[2])
            self.team2.add_player(all_players[3])

    def is_valid(self):
        if len(self.players) != 4:
            return False

        # Count players by skill level
        beginner_count = sum(1 for p in self.players if p.get_skill_level() == SkillLevel.BEGINNER)
        intermediate_count = sum(1 for p in self.players if p.get_skill_level() == SkillLevel.INTERMEDIATE)
        advanced_count = sum(1 for p in self.players if p.get_skill_level() == SkillLevel.ADVANCED)

        # Invalid: 2 beginners + 2 advanced (Beginner+Advanced without Intermediate)
        if beginner_count == 2 and advanced_count == 2 and intermediate_count == 0:
            return False

        # Invalid: exactly 2 beginners + 2 intermediate
        if beginner_count == 2 and intermediate_count == 2 and advanced_count == 0:
            return False

        # Invalid: Beginner + Advanced without Intermediate
        if beginner_count > 0 and advanced_count > 0 and intermediate_count == 0:
            return False

        return True

    def __str__(self):
        sb = []
        if self.is_forced:
            sb.append(f"Forced Group {self.group_number}:\n")
        else:
            sb.append(f"Group {self.group_number}:\n")
        for player in self.players:
            sb.append(f"  - {str(player)}\n")
        return "".join(sb)