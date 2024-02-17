#Elijah Turany
#02/16/2024
#Candidate Class File
class Candidate:
    eliminated = False
    winner = False
    name = ""
    votes = []
    votePercent = []

    #Constructor
    def __init__(self, nameIn):
        self.name = nameIn
        self.votes = [0]
        self.votePercent = [0]
        
    def getName(self):
        return self.name
    
    def getEliminated(self):
        return self.eliminated
    
    def getVotes(self, roundNum):
        #Returns 0 if candidate didn't get vote for during roundNum
        if roundNum >= len(self.votes):
            return 0
        return self.votes[roundNum]

    def getVotePercent(self, roundNum):
        #Returns 0 if candidate didn't get vote for during roundNum
        if roundNum >= len(self.votePercent):
            return 0
        return self.votePercent[roundNum]
    
    def setVotePercent(self, roundNum, val):
        if roundNum == len(self.votePercent):
            self.votePercent.append(0) 
        self.votePercent[roundNum] = val

    def addVote(self,roundNum): 
        if roundNum == len(self.votes):
            self.votes.append(0)           
        self.votes[roundNum] += 1

    def eliminate(self):
        self.eliminated = True

    