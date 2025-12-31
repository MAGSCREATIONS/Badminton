from player import Player, SkillLevel
from badminton_group_randomizer import BadmintonGroupRandomizer

def main():
    print("=== Badminton Player Group Randomizer ===\n")
    print("This app randomizes players into groups of 4.")
    print("Groups consist of: Beginner+Intermediate OR Intermediate+Advanced")
    print("Never: Beginner+Advanced\n")

    # Fixed list of players
    players = []

    # Beginner players (4)
    players.append(Player("Balaji", SkillLevel.BEGINNER))
    players.append(Player("Anand", SkillLevel.BEGINNER))
    players.append(Player("Prakash", SkillLevel.BEGINNER))
    players.append(Player("Sree", SkillLevel.BEGINNER))

    # Intermediate players (10)
    players.append(Player("Arun", SkillLevel.INTERMEDIATE))
    players.append(Player("Dileep", SkillLevel.INTERMEDIATE))
    players.append(Player("Bheesh", SkillLevel.INTERMEDIATE))
    players.append(Player("Kirshnamurthy", SkillLevel.INTERMEDIATE))
    players.append(Player("Joseph", SkillLevel.INTERMEDIATE))
    players.append(Player("Hashim", SkillLevel.INTERMEDIATE))
    players.append(Player("Santhosh", SkillLevel.INTERMEDIATE))
    players.append(Player("Sudha", SkillLevel.INTERMEDIATE))
    players.append(Player("Suren", SkillLevel.INTERMEDIATE))
    players.append(Player("Kripa", SkillLevel.INTERMEDIATE))

    # Advanced players (5)
    players.append(Player("Charles", SkillLevel.ADVANCED))
    players.append(Player("Faizee", SkillLevel.ADVANCED))
    players.append(Player("Raaju", SkillLevel.ADVANCED))
    players.append(Player("Arvind", SkillLevel.ADVANCED))
    players.append(Player("Raja", SkillLevel.ADVANCED))

    print("Players list:")
    print("  Beginners: 4")
    print("  Intermediates: 10")
    print("  Advanced: 5")
    print(f"  Total: {len(players)} players\n")

    # Get absent players
    absent_input = input("Enter names of absent players (comma-separated, or press Enter for none):\nAbsent players: ").strip()

    absent_names = set()
    if absent_input:
        names = [name.strip() for name in absent_input.split(",")]
        absent_names.update(names)

    # Filter out absent players
    present_players = []
    absent_found = []
    for player in players:
        if player.get_name() in absent_names:
            absent_found.append(player.get_name())
        else:
            present_players.append(player)

    if absent_found:
        print(f"\nMarked as absent: {', '.join(absent_found)}")

    print(f"\nPresent players: {len(present_players)}")
    if len(present_players) < 4:
        print("Error: Need at least 4 present players to form groups!")
        return

    print("Randomizing into groups...\n")

    try:
        groups = BadmintonGroupRandomizer.randomize_players(present_players)

        if not groups:
            print("Could not form any valid groups with the given players.")
        else:
            print("=== Groups Formed ===\n")
            for group in groups:
                print(str(group))
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()