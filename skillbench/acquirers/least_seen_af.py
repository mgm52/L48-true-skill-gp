from skillbench import emulators
from skillbench.acquirer import AcquisitionFunction, compatible_emulators
from skillbench.data import Team, TeamPair
from skillbench.emulator import Emulator
from skillbench import emulators
import random
import math

@compatible_emulators()
class LeastSeenAcquisitionFunction(AcquisitionFunction):
    def __call__(self, emu: Emulator, teams: TeamPair) -> float:
        super().__call__(emu, teams)
        team1, team2 = teams
        # One information-theoretic approach: assume that the more times a team has been seen, the more information we have about it, logarithmically
        count1, count2 = emu.team_fit_count.get(team1, 0), emu.team_fit_count.get(team2, 0)
        information = -1 * (math.log(count1+1) + math.log(count2+1))
        return information

if __name__ == "__main__":
    lsaf = LeastSeenAcquisitionFunction()
    wr_emu = emulators.WinRateEmulator()
    print(lsaf.compatible_emulators)
    print(lsaf(wr_emu, TeamPair(Team("A"), Team("B"), random)))
    print(lsaf.name)
