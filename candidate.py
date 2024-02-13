class Candidate:
    eliminated = False
    winner = False
    name = ""
    votes, votePercent = []

    def __init__(self, nameIn):
        self.name = nameIn
        self.votes = [0]
        self.votePercent = [0]
        
    def getName(self):
        return self.name
    
    def getEliminated(self):
        return self.eliminated
    
    def getVotes(self, roundNum):
        return self.votes[roundNum]

    def eliminate(self):
        self.eliminated = True

    def addVote(self,roundNum):            
        self.votes[roundNum] += 1