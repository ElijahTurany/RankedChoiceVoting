#Elijah Turany
#02/16/2024
#Candidate Class File
class Candidate:
    eliminated = False
    roundEliminated = -1
    winner = False
    winRound = -1
    tie = False
    tieRound = -1
    name = ""
    votes = []
    votePercent = []


    #Constructor
    def __init__(self, nameIn):
        self.name = nameIn
        self.votes = [0]
        self.votePercent = [0]

    def setWinner(self, roundNum):
        self.winner = True
        self.winRound = roundNum

    def setTie(self, roundNum):
        self.tie = True
        self.eliminated = False
        self.roundEliminated = -1
        self.tieRound = roundNum
        
    def getName(self):
        return self.name
    
    def getEliminated(self):
        return self.eliminated
    
    def getVotes(self, roundNum):
        #Returns 0 if candidate didn't get vote for during roundNum
        if(roundNum >= len(self.votes)):
            return 0
        return self.votes[roundNum]

    def getVotePercent(self, roundNum):
        #Returns 0 if candidate didn't get vote for during roundNum
        if(roundNum >= len(self.votePercent)):
            return 0
        return self.votePercent[roundNum]
    
    def setVotePercent(self, roundNum, val):
        if(roundNum == len(self.votePercent)):
            self.votePercent.append(0) 
        self.votePercent[roundNum] = val

    def addVote(self,roundNum): 
        if(roundNum == len(self.votes)):
            self.votes.append(0)           
        self.votes[roundNum] += 1

    def eliminate(self, roundNum):
        self.eliminated = True
        self.roundEliminated = roundNum

    def getRoundResult(self, roundNum):
        returnVal = self.name + ", "
        #Adds vote and vote percent to results
        if(roundNum >= len(self.votes)):
            returnVal += "0 votes, 0% of vote"
        else:    
            returnVal += str(self.votes[roundNum]) + " votes, " + str(round(self.votePercent[roundNum]*100, 2)) + "% of vote"

        #Adds a summary of status in race to results
        if(self.winRound == roundNum):
            returnVal += ", Winner at Round: " + str(self.winRound + 1)
        elif(self.tieRound == roundNum):
            returnVal += ", Tied at Round: " + str(self.tieRound + 1)
        elif(self.eliminated and self.roundEliminated == roundNum):
            returnVal += ", Eliminated at Round: " + str(self.roundEliminated  + 1)
        elif(self.eliminated and self.roundEliminated < roundNum):
            returnVal += ", Previously Eliminated at Round: " + str(self.roundEliminated  + 1)
        else:
            returnVal += ", Still in Running at Round: " + str(roundNum  + 1)
        return(returnVal)

    