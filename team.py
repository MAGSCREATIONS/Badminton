from player import Player

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        if len(self.players) >= 2:
            raise ValueError("Team is full (2 players maximum)")
        self.players.append(player)

    def get_players(self):
        return self.players.copy()

    def get_team_name(self):
        return self.team_name

    def is_full(self):
        return len(self.players) == 2

    def __str__(self):
        player_names = [p.get_name() for p in self.players]
        return f"{self.team_name}: {' & '.join(player_names)}"