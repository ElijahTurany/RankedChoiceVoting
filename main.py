import csv

class candidate:
    eliminated = False
    winner = False
    name = ""
    votePercent = []

    def __init__(self, nameIn):
        self.name = nameIn
        self.votes = [0]
        
    def getName(self):
        return self.name
    
    def getEliminated(self):
        return self.eliminated

    def eliminate(self):
        self.eliminated = True

    def addVote(self,roundNum):
        self.votes[roundNum] += 1
        print(self.name)
        print(self.votes[0])    


class BallotProccessor:
    candidates = dict()
    candidateNames = set()
    def loadBallots(self,filename):
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                #Normalize Ballots
                self.candidateNames.add(row[0])
                self.candidateNames.add(row[1])
                self.candidateNames.add(row[2])
            print(self.candidateNames)
            for i in self.candidateNames:
                #Creates a candidate object with each name and adds it to a dictionary bound to its name
                c = candidate(i)
                self.candidates[i] = c
            #for i in self.candidates:
                #print(i.getName())
            self.runRound(self,filename, 0)
    
    def runRound(self,filename, roundNum):
        min = []
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                for i in range(3):
                    if(row[i] != ""):
                        #print(self.candidates[row[i]].getName())
                        if(not self.candidates[row[i]].getEliminated()):
                            #self.candidates[row[i]].votes.append(0)
                            self.candidates[row[i]].addVote(roundNum)
                            print("Voted")
                            for i in self.candidateNames:
                                print(self.candidates[i].votes[0])
                            break
            #Find min, eliminate 0 votes
            for i in self.candidateNames:
                if self.candidates[i].votes[roundNum] == 0:
                    self.candidates[i].eliminate()
                    print("Eliminated:")
                    print(self.candidates[i].getName())
                elif len(min) == 0:
                    min.append(self.candidates[i])
                elif self.candidates[i].votes[roundNum] == min[0].votes[roundNum]:
                    min.append(self.candidates[i])
                elif self.candidates[i].votes[roundNum] < min[0].votes[roundNum]:
                    min.clear()
                    min.append(self.candidates[i])
                
            print("Eliminated:")
            print(min[0].getName())


              

BP = BallotProccessor

BP.loadBallots(BP,"SmallListBallots.csv")

c = candidate("test")
