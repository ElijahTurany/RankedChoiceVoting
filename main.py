import csv

class candidate:
    eliminated = False
    winner = False
    name = ""

    def __init__(self, nameIn):
        self.name = nameIn
        self.votes = [0]
        self.votePercent = [0]
        
    def getName(self):
        return self.name
    
    def getEliminated(self):
        return self.eliminated

    def eliminate(self):
        self.eliminated = True

    def addVote(self,roundNum):            
        self.votes[roundNum] += 1
        print(self.name)
        print(self.votes[roundNum])    


class BallotProccessor:
    candidates = dict()
    candidateNames = set()
    roundVotes = [0]
    winner = None
    def loadBallots(self,filename):
        #CSV file reader
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            #Adds every name in each row of csv file to candidateNames. Only unique names are accepted
            for row in csv_reader:
                #Normalize Ballots
                self.candidateNames.add(row[0])
                self.candidateNames.add(row[1])
                self.candidateNames.add(row[2])
            print(self.candidateNames)
            #Creates a candidate object with each name and adds it to a dictionary bound to its name
            for i in self.candidateNames:
                c = candidate(i)
                self.candidates[i] = c
            #Starts vote counting proccess with running round 0
            self.runRound(self,filename, 0)
    
    def runRound(self,filename, roundNum):
        self.roundVotes.append(0)
        #CSV file reader
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for i in range(3):
                    #Checks if vote is left blank
                    if(row[i] != ""):
                        #Checks if candidate is eliminated
                        if(not self.candidates[row[i]].getEliminated()):
                            #Adds a vote to first valid candidate
                            self.candidates[row[i]].addVote(roundNum)
                            #Increments the number of votes cast this round
                            self.roundVotes[roundNum] += 1
                            print("Voted")
                            for i in self.candidateNames:
                                print(self.candidates[i].votes[0])
                            break
            #Minimum votes is defined as an array because there may be a tie for lowest votes
            min = []
            #Find min, eliminate 0 votes
            print("*")
            for i in self.candidateNames:
                #Calculate vote percent
                self.candidates[i].votes.append(0)
                self.candidates[i].votePercent.append(0)
                #print(len(self.candidates[i].votes))
                self.candidates[i].votePercent[roundNum] = self.candidates[i].votes[roundNum] / self.roundVotes[roundNum]
                if self.candidates[i].votePercent[roundNum] > .5:
                    winner = self.candidates[i]
                    print("p")
                #Eliminates candidate if they got 0 votes
                if self.candidates[i].votes[roundNum] == 0:
                    self.candidates[i].eliminate()
                    print("Eliminated: " + self.candidates[i].getName())
                #Adds candidate to min array if this is the first candidate checked
                elif len(min) == 0:
                    min.append(self.candidates[i])
                #Adds candidate to min array if they tie for lowest votes
                elif self.candidates[i].votes[roundNum] == min[0].votes[roundNum]:
                    min.append(self.candidates[i])
                #Clears min array and adds candidate if they have a lower number of votes
                elif self.candidates[i].votes[roundNum] < min[0].votes[roundNum]:
                    min.clear()
                    min.append(self.candidates[i])

            #Tie Checking    
            print("Eliminated: " + min[0].getName())
            print(min[0].votePercent[roundNum])

            if self.winner != None:
                print("Winner: " + self.winner.getName())
                print(self.winner.votePercent[roundNum])
            #else:
                #self.runRound(self,filename, roundNum + 1)
            print(self.candidates["Dalinar Kholin"].votePercent[roundNum])


              

BP = BallotProccessor

BP.loadBallots(BP,"TestBallot1.csv")

c = candidate("test")
