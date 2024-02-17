#Elijah Turany
#02/16/2024
#Python Main File
from ballotproccessor import BallotProccessor

BP = BallotProccessor

BP.loadBallots(BP,"SmallListBallots.csv", 3)
BP.clearBallot(BP)
BP.loadBallots(BP,"TestBallot1.csv", 3)
BP.clearBallot(BP)
BP.loadBallots(BP,"LargeListBallots.csv",3)
