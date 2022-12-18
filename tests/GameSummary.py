import json
import re

class GameSummary:
    number_of_players = 0

    def __init__(self, file_name, map_name, map_size, duration, timestamp, diplomacy_type, members):

        self.game_name = re.search("@.*[0-9] ", file_name).group(0)
        self.game_version = re.search("v([^\s]+)", file_name).group(0)
        self.map_name = map_name
        self.map_size = map_size
        self.duration = duration
        self.timestamp = timestamp
        self.diplomacy_type = diplomacy_type
        self.members = members
        self.number_of_players = len(members)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
