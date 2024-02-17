#Elijah Turany
#02/16/2024
#Python Main File
from ballotproccessor import BallotProccessor
import unittest

class TestBallotProccessor(unittest.TestCase):
    def testSmallBallot(self):
        self.maxDiff = None
        BP = BallotProccessor
        BP.clearBallot(BP)

        BP.loadBallots(BP, "SmallListBallots.csv", 3)
        self.assertEqual(BP.getRoundResult(BP,1), "Round 1\nJasnah Kholin, 0 votes, 0.0% of vote, Eliminated at Round: 1\nKaladin Stormblessed, 0 votes, 0.0% of vote, Eliminated at Round: 1\nMeridas Amaram, 0 votes, 0.0% of vote, Eliminated at Round: 1\nRenarin Kholin, 0 votes, 0.0% of vote, Eliminated at Round: 1\nShallan Davar, 0 votes, 0.0% of vote, Eliminated at Round: 1\nTorol Sadeas, 4 votes, 40.0% of vote, Eliminated at Round: 1\nDalinar Kholin, 6 votes, 60.0% of vote, Winner at Round: 1\n")

    def testLargeBallot(self):
        self.maxDiff = None
        BP = BallotProccessor
        BP.clearBallot(BP)

        BP.loadBallots(BP, "LargeListBallots.csv", 3)
        self.assertEqual(BP.getRoundResult(BP,1), "Round 1\nRenarin Kholin, 0 votes, 0.0% of vote, Eliminated at Round: 1\nMeridas Amaram, 1 votes, 0.99% of vote, Eliminated at Round: 1\nJasnah Kholin, 2 votes, 1.98% of vote, Still in Running at Round: 1\nShallan Davar, 6 votes, 5.94% of vote, Still in Running at Round: 1\nKaladin Stormblessed, 16 votes, 15.84% of vote, Still in Running at Round: 1\nTorol Sadeas, 32 votes, 31.68% of vote, Still in Running at Round: 1\nDalinar Kholin, 44 votes, 43.56% of vote, Still in Running at Round: 1\n")
        self.assertEqual(BP.getRoundResult(BP,2), "Round 2\nMeridas Amaram, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nRenarin Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nJasnah Kholin, 2 votes, 1.98% of vote, Eliminated at Round: 2\nShallan Davar, 6 votes, 5.94% of vote, Still in Running at Round: 2\nKaladin Stormblessed, 16 votes, 15.84% of vote, Still in Running at Round: 2\nTorol Sadeas, 33 votes, 32.67% of vote, Still in Running at Round: 2\nDalinar Kholin, 44 votes, 43.56% of vote, Still in Running at Round: 2\n")
        self.assertEqual(BP.getRoundResult(BP,3), "Round 3\nMeridas Amaram, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nRenarin Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nJasnah Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 2\nShallan Davar, 6 votes, 5.94% of vote, Eliminated at Round: 3\nKaladin Stormblessed, 16 votes, 15.84% of vote, Still in Running at Round: 3\nTorol Sadeas, 33 votes, 32.67% of vote, Still in Running at Round: 3\nDalinar Kholin, 46 votes, 45.54% of vote, Still in Running at Round: 3\n")
        self.assertEqual(BP.getRoundResult(BP,4), "Round 4\nMeridas Amaram, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nRenarin Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nJasnah Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 2\nShallan Davar, 0 votes, 0% of vote, Previously Eliminated at Round: 3\nKaladin Stormblessed, 17 votes, 17.35% of vote, Eliminated at Round: 4\nTorol Sadeas, 33 votes, 33.67% of vote, Still in Running at Round: 4\nDalinar Kholin, 48 votes, 48.98% of vote, Still in Running at Round: 4\n")
        self.assertEqual(BP.getRoundResult(BP,5), "Round 5\nMeridas Amaram, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nRenarin Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nJasnah Kholin, 0 votes, 0% of vote, Previously Eliminated at Round: 2\nShallan Davar, 0 votes, 0% of vote, Previously Eliminated at Round: 3\nKaladin Stormblessed, 0 votes, 0% of vote, Previously Eliminated at Round: 4\nTorol Sadeas, 33 votes, 38.82% of vote, Eliminated at Round: 5\nDalinar Kholin, 52 votes, 61.18% of vote, Winner at Round: 5\n")
        self.assertEqual(BP.getRoundResult(BP,6), None)

    def testMissingVotes(self):
        self.maxDiff = None
        BP = BallotProccessor
        BP.clearBallot(BP)

        BP.loadBallots(BP, "MissingVotesBallot.csv", 3)
        self.assertEqual(BP.getRoundResult(BP,1), "Round 1\nC, 1 votes, 14.29% of vote, Eliminated at Round: 1\nA, 3 votes, 42.86% of vote, Still in Running at Round: 1\nB, 3 votes, 42.86% of vote, Still in Running at Round: 1\n")
        self.assertEqual(BP.getRoundResult(BP,2), "Round 2\nC, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nB, 3 votes, 42.86% of vote, Eliminated at Round: 2\nA, 4 votes, 57.14% of vote, Winner at Round: 2\n")

    def testOver50Percent(self):
        self.maxDiff = None
        BP = BallotProccessor
        BP.clearBallot(BP)

        BP.loadBallots(BP, "Over50PercentBallot.csv", 3)
        self.assertEqual(BP.getRoundResult(BP,1), "Round 1\nB, 1 votes, 20.0% of vote, Eliminated at Round: 1\nA, 4 votes, 80.0% of vote, Winner at Round: 1\n")

    def testTieVote(self):
        self.maxDiff = None
        BP = BallotProccessor
        BP.clearBallot(BP)

        BP.loadBallots(BP, "TieVoteBallot.csv", 3)
        self.assertEqual(BP.getRoundResult(BP,1), "Round 1\nD, 0 votes, 0.0% of vote, Eliminated at Round: 1\nE, 0 votes, 0.0% of vote, Eliminated at Round: 1\nC, 1 votes, 20.0% of vote, Eliminated at Round: 1\nA, 2 votes, 40.0% of vote, Still in Running at Round: 1\nB, 2 votes, 40.0% of vote, Still in Running at Round: 1\n")
        self.assertEqual(BP.getRoundResult(BP,2), "Round 2\nC, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nD, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nE, 0 votes, 0% of vote, Previously Eliminated at Round: 1\nA, 2 votes, 50.0% of vote, Tied at Round: 2\nB, 2 votes, 50.0% of vote, Tied at Round: 2\n")

unittest.main()
