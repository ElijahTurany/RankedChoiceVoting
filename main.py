#Elijah Turany
#02/16/2024
#Python Main File
from ballotproccessor import BallotProccessor

BP = BallotProccessor

BP.loadBallots(BP,"SmallListBallots.csv", 3)
BP.getRoundResult(BP, 1)
BP.clearBallot(BP)
BP.loadBallots(BP,"TestBallot1.csv", 3)
print(BP.getRoundResult(BP, 1))
print(BP.getRoundResult(BP, 2))
#BP.clearBallot(BP)
#BP.loadBallots(BP,"LargeListBallots.csv",3)
#BP.getRoundResult(BP,1)
#BP.getRoundResult(BP,2)
#BP.getRoundResult(BP,3)
#BP.getRoundResult(BP,4)
#BP.getRoundResult(BP,5)
#BP.getRoundResult(BP,6)

