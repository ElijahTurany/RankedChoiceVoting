from ballotproccessor import BallotProccessor

BP = BallotProccessor

BP.loadBallots(BP,"SmallListBallots.csv")
BP.clearBallot(BP)
BP.loadBallots(BP,"TestBallot1.csv")
#BP.loadBallots(BP,"LargeListBallots.csv")
