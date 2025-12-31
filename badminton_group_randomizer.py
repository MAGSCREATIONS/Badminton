import random
from player import Player, SkillLevel
from group import Group

class BadmintonGroupRandomizer:

    @staticmethod
    def _try_form_group(beginners, intermediates, advanced, group_number):
        # Try different valid combinations in random order
        combinations = []

        # Beginner + Intermediate combinations (avoiding 2B+2I)
        if len(beginners) >= 1 and len(intermediates) >= 3:
            combinations.append((1, 3, 0))  # 1B + 3I
        if len(beginners) >= 3 and len(intermediates) >= 1:
            combinations.append((3, 1, 0))  # 3B + 1I

        # Intermediate + Advanced combinations (all allowed: 1I+3A, 2I+2A, 3I+1A)
        if len(intermediates) >= 1 and len(advanced) >= 3:
            combinations.append((0, 1, 3))  # 1I + 3A
        if len(intermediates) >= 2 and len(advanced) >= 2:
            combinations.append((0, 2, 2))  # 2I + 2A
        if len(intermediates) >= 3 and len(advanced) >= 1:
            combinations.append((0, 3, 1))  # 3I + 1A

        # All Intermediate (4I)
        if len(intermediates) >= 4:
            combinations.append((0, 4, 0))  # 4I

        # Shuffle combinations for randomization
        random.shuffle(combinations)

        # Try each combination
        for combo in combinations:
            b_needed, i_needed, a_needed = combo

            if len(beginners) >= b_needed and len(intermediates) >= i_needed and len(advanced) >= a_needed:

                group = Group(group_number)

                # Add players according to combination
                for _ in range(b_needed):
                    group.add_player(beginners.pop(0))
                for _ in range(i_needed):
                    group.add_player(intermediates.pop(0))
                for _ in range(a_needed):
                    group.add_player(advanced.pop(0))

                if group.is_valid():
                    return group
                else:
                    # Return players if invalid
                    for p in group.get_players():
                        if p.get_skill_level() == SkillLevel.BEGINNER:
                            beginners.append(p)
                        elif p.get_skill_level() == SkillLevel.INTERMEDIATE:
                            intermediates.append(p)
                        elif p.get_skill_level() == SkillLevel.ADVANCED:
                            advanced.append(p)

        return None

    @staticmethod
    def randomize_players(players):
        if not players or len(players) == 0:
            raise ValueError("Player list cannot be empty")

        # Shuffle players for randomization
        shuffled_players = players.copy()
        random.shuffle(shuffled_players)

        # Separate players by skill level
        beginners = [p for p in shuffled_players if p.get_skill_level() == SkillLevel.BEGINNER]
        intermediates = [p for p in shuffled_players if p.get_skill_level() == SkillLevel.INTERMEDIATE]
        advanced = [p for p in shuffled_players if p.get_skill_level() == SkillLevel.ADVANCED]

        groups = []
        group_number = 1

        remaining_beginners = beginners.copy()
        remaining_intermediates = intermediates.copy()
        remaining_advanced = advanced.copy()

        # Try to form groups with all possible valid combinations
        while True:
            group = BadmintonGroupRandomizer._try_form_group(
                remaining_beginners, remaining_intermediates, remaining_advanced, group_number
            )

            if group and len(group.get_players()) == 4 and group.is_valid():
                groups.append(group)
                group_number += 1
            else:
                if group:
                    # Return players to pools if group couldn't be formed
                    for p in group.get_players():
                        if p.get_skill_level() == SkillLevel.BEGINNER:
                            remaining_beginners.append(p)
                        elif p.get_skill_level() == SkillLevel.INTERMEDIATE:
                            remaining_intermediates.append(p)
                        elif p.get_skill_level() == SkillLevel.ADVANCED:
                            remaining_advanced.append(p)
                break  # No more groups can be formed

        # Handle any remaining players - create a forced group
        remaining_players = remaining_beginners + remaining_intermediates + remaining_advanced

        if remaining_players:
            # Create a forced group with remaining players
            forced_group = Group(group_number, True)

            # Add up to 4 players to the forced group
            players_to_add = min(4, len(remaining_players))
            for i in range(players_to_add):
                forced_group.add_player(remaining_players[i])

            groups.append(forced_group)

            # If there are more than 4 remaining players, create additional forced groups
            remaining_count = len(remaining_players) - players_to_add
            while remaining_count > 0:
                group_number += 1
                additional_forced_group = Group(group_number, True)
                add_count = min(4, remaining_count)
                for i in range(players_to_add, players_to_add + add_count):
                    additional_forced_group.add_player(remaining_players[i])
                groups.append(additional_forced_group)
                players_to_add += add_count
                remaining_count -= add_count

        # Split all groups into teams
        for group in groups:
            if len(group.get_players()) == 4:
                group.split_into_teams()

        return groups