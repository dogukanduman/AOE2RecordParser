import json


class Member:
    def __init__(self, civilization, name, prefer_random, color, winner):
        self.civilization = civilization
        self.name = name
        self.prefer_random = prefer_random
        self.color = color
        self.winner = winner

    def get_as_json(self):
        return json.dumps(self)
