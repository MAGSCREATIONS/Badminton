from flask import Flask, render_template, request, jsonify
from player import Player, SkillLevel
from badminton_group_randomizer import BadmintonGroupRandomizer
import json

app = Flask(__name__)

# Fixed list of players
PLAYERS = [
    Player("Balaji", SkillLevel.BEGINNER),
    Player("Anand(Forever in our memories)", SkillLevel.BEGINNER),
    Player("Prakash", SkillLevel.BEGINNER),
    Player("Sree", SkillLevel.BEGINNER),
    Player("Arun", SkillLevel.INTERMEDIATE),
    Player("Dileep", SkillLevel.INTERMEDIATE),
    Player("Bheesh", SkillLevel.INTERMEDIATE),
    Player("Kirshnamurthy", SkillLevel.INTERMEDIATE),
    Player("Joseph", SkillLevel.INTERMEDIATE),
    Player("Hashim", SkillLevel.INTERMEDIATE),
    Player("Santhosh", SkillLevel.INTERMEDIATE),
    Player("Sudha", SkillLevel.INTERMEDIATE),
    Player("Suren", SkillLevel.INTERMEDIATE),
    Player("Kripa", SkillLevel.INTERMEDIATE),
    Player("Charles", SkillLevel.ADVANCED),
    Player("Faizee", SkillLevel.ADVANCED),
    Player("Raaju", SkillLevel.ADVANCED),
    Player("Arvind", SkillLevel.ADVANCED),
    Player("Raja", SkillLevel.ADVANCED),
]

@app.route('/')
def index():
    return render_template('index.html', players=PLAYERS)

@app.route('/randomize', methods=['POST'])
def randomize():
    data = request.get_json()
    present_player_names = data.get('present_players', [])

    # Filter present players
    present_players = [p for p in PLAYERS if p.get_name() in present_player_names]

    if len(present_players) < 4:
        return jsonify({'error': 'Need at least 4 present players to form groups!'})

    try:
        groups = BadmintonGroupRandomizer.randomize_players(present_players)

        groups_data = []
        for group in groups:
            group_data = {
                'group_number': group.get_group_number(),
                'is_forced': group.is_forced,
                'players': [{'name': p.get_name(), 'skill': p.get_skill_level().value} for p in group.get_players()],
                'teams': []
            }

            if group.get_team1():
                team1_data = {
                    'name': group.get_team1().get_team_name(),
                    'players': [p.get_name() for p in group.get_team1().get_players()]
                }
                group_data['teams'].append(team1_data)

            if group.get_team2():
                team2_data = {
                    'name': group.get_team2().get_team_name(),
                    'players': [p.get_name() for p in group.get_team2().get_players()]
                }
                group_data['teams'].append(team2_data)

            groups_data.append(group_data)

        return jsonify({'groups': groups_data})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
