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


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        path = "/Users/dogukanduman/Downloads/aoc-mgz-master/tests/savegame/read/"
        self.files = []

        for file in self.get_files(path):
            self.files.append(file)

    def test_version(self):
        number_of_read_file = 0
        number_of_files = 0
        game_summaries = {}
        # print(f"Number of Files: {len(self.files)}")
        for file_name in self.files:
            game_summary = self.get_summary_of_file("/Users/dogukanduman/Downloads/aoc-mgz-master/tests/savegame/read/",
                                                    file_name)
            if game_summary is not None:
                number_of_read_file = number_of_read_file + 1
                game_summaries["Game " + game_summary.timestamp] = game_summary.to_json()
                self.write_summary_to_file(game_summary)
            number_of_files = number_of_files + 1
            # print(f"Number of Read Files: {number_of_files}/{len(self.files)}")

        # print(f"Number of Read Files: {number_of_read_file}/{number_of_files}")




    def write_summary_to_file(self, game_summary):
        print(game_summary.to_json())
        json_game_summary = game_summary.to_json()
        json_file = open("ageofresults.json", "a")
        json_file.write(json_game_summary)
        json_file.write("\n")
        json_file.close()

    def get_summary_of_file(self, path, file_name):

        # print(file_name)
        try:
            full_path = os.path.join(path, file_name)
            with open(full_path, 'rb') as handle:
                parsed_match = parse_match(handle)
                members = []
                for team in parsed_match.teams:
                    for member in team:
                        m = Member(member.civilization, member.name, str(member.prefer_random), member.color,
                                   str(member.winner))
                        members.append(m)

            game_summary = GameSummary(file_name, parsed_match.map.name, parsed_match.map.size,
                                       str(parsed_match.duration),
                                       str(parsed_match.timestamp), parsed_match.diplomacy_type, members)

        except BaseException as exception:
            # print(f"Exception Name: {type(exception).__name__}")
            # print(f"Exception Desc: {exception}")
            return None
        # print("-------------------------------------")

        # shutil.move(full_path, "/Users/dogukanduman/Downloads/aoc-mgz-master/tests/savegame/read/")
        return game_summary

    @staticmethod
    def get_files(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                yield file
