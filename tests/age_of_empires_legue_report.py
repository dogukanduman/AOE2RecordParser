import unittest
import os
import json
import shutil
from time import sleep
from mgz.fast.header import parse
from mgz.util import Version
from mgz.summary import Summary
from GameSummary import GameSummary
from Member import Member
from mgz.model import parse_match
import glob
from datetime import datetime
from datetime import timedelta
from datetime import time

class ReadTestModel(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("hello")

    def test_read_result_file(self):
        file = open('/Users/dogukanduman/Downloads/aoc-mgz-master/tests/ageofresults.json', 'r')
        lines = file.readlines()

        players_with_matches = {}
        matches = {}
        game_summaries = []
        for index, line in enumerate(lines):
            # print("Line {}: {}".format(index, line.strip()))
            game_summaries.append(json.loads(line.strip()))
        file.close()

        index = 0
        for game_summary in game_summaries:
            matches[index] = game_summary
            index = index + 1

        for key in matches:
            match = matches[key]

            if self.filter_matches(match):
                members = match["members"]


        #         for member in members:
        #             match_player_info = dict(member)
        #             match_player_info["game_id"] = key
        #             member_name = match_player_info["name"]
        #             match_list = players_with_matches.get(member_name, [])
        #             match_list.append(match_player_info)
        #             players_with_matches[member_name] = match_list
        #
        # for player in players_with_matches:
        #
        #     player_with_matches = players_with_matches[player]
        #     if len(player_with_matches) > 3:
        #         print(player)
        #         self.calculate_stats(player_with_matches)

    def calculate_stats(self, player_with_matches):

        civilization_stats = {}
        color_stats = {}
        win_stats = {}
        for match_player_info in player_with_matches:
            civilization = match_player_info['civilization']
            color = match_player_info['color']
            winner = match_player_info['winner']

            civilization_counter = civilization_stats.get(civilization, 0)
            civilization_counter = civilization_counter + 1
            civilization_stats[civilization] = civilization_counter

            color_counter = color_stats.get(color, 0)
            color_counter = color_counter + 1
            color_stats[color] = color_counter

            winner_counter = win_stats.get(winner, 0)
            winner_counter = winner_counter + 1
            win_stats[winner] = winner_counter

        print(sorted(civilization_stats.items(), key=lambda x: x[1], reverse=True))
        print(sorted(color_stats.items(), key=lambda x: x[1], reverse=True))
        print(win_stats)


    #def calculate_league_report

    def filter_matches(self, match):
        friend_list = ["ongundogdu", "hannibal13", "phankarlo", "tokmak", "Pulpos888", "chibraist", "avemrah_duman",
                       "onemangang"]
        members = match["members"]
        for member in members:
            match_player_info = dict(member)
            player_name = match_player_info["name"]
            if player_name not in friend_list:
                return False

        if match["diplomacy_type"] != "TG":
            return False

        if datetime.strptime(match["duration"], '%H:%M:%S.%f').time() < time(0, 15, 0):
            print(match)
            return False
        return True
