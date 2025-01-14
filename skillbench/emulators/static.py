from skillbench.emulator import Emulator
from trueskill import TrueSkill
import itertools
import math
import matplotlib.pyplot as plt
from skillbench.data import Team, TeamPair


class StaticEmulator(Emulator):
    def __init__(self):
        super().__init__()
        pass

    def emulate(self, team1, team2):
        # Randomness can still come from TeamPair's shuffling of team1, team2
        return 1

    def fit_one_match(self, teams: TeamPair, winner: Team):
        super().fit_one_match(teams, winner)
        pass

    @property
    def name(self):
        return "StaticEmulator"
