#Elijah Turany
#02/16/2024
#BallotProccessor Class File
import csv
from candidate import Candidate

class BallotProccessor:
    candidates = dict()
    candidateNames = set()
    roundVotes = [0]
    numEliminated = 0
    winner = []
    rounds = 0
    
    #Resets variables so ballot proccessor may be used again 
    def clearBallot(self):
        self.candidates.clear()
        self.candidateNames.clear()
        self.roundVotes = [0]
        self.numEliminated = 0
        self.winner.clear()
        self.rounds = 0


    #Given a filename and number of slots on ballot, loads the ballot and starts the vote counting proccess
    def loadBallots(self, filename, numSlots):

        #CSV file reader
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')

            #Adds every name in each row of csv file to candidateNames. Only unique names are accepted
            self.candidateNames.add("")
            for row in csv_reader:
                self.candidateNames.add(row[0])
                self.candidateNames.add(row[1])
                self.candidateNames.add(row[2])
            self.candidateNames.remove("")
            #print(self.candidateNames)

            #Creates a candidate object with each name and adds it to a dictionary bound to its name
            for i in self.candidateNames:
                c = Candidate(i)
                self.candidates[i] = c

            #Starts vote counting proccess with running round 0
            self.runRound(self, filename, 0, numSlots)
    
    #Runs a round of voting using a given filename and given round number
    def runRound(self, filename, roundNum, numSlots):
        self.roundVotes.append(0)
        
        #CSV file reader
        with open(filename) as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                #
                for i in range(numSlots):

                    #Checks if vote is left blank
                    if(row[i] != ""):
                        #Checks if candidate is eliminated
                        if(not self.candidates[row[i]].getEliminated()):

                            #Adds a vote to first valid candidate
                            self.candidates[row[i]].addVote(roundNum)

                            #Increments the number of votes cast this round, and continues to next row
                            self.roundVotes[roundNum] += 1
                            break
                        
            #for i in self.candidateNames:
            #    print(self.candidates[i].getName() + ": " + str(self.candidates[i].getVotes(roundNum)))  

            #Minimum votes is defined as an array because there may be a tie for lowest votes
            min = []
            #Find min, eliminate 0 votes
            for i in self.candidateNames:

                #Calculate vote percent
                self.candidates[i].setVotePercent(roundNum, self.candidates[i].getVotes(roundNum) / self.roundVotes[roundNum])

                #Add candidate to winner array if they have over 50% of the vote
                if(self.candidates[i].getVotePercent(roundNum) > .5):
                    self.winner.append(self.candidates[i])

                #Eliminates candidate if they got 0 votes and not already eliminated
                if(self.candidates[i].getEliminated() == True):
                    pass
                elif(self.candidates[i].getVotes(roundNum) == 0):
                    self.candidates[i].eliminate(roundNum)
                    self.numEliminated += 1
                    #print("Eliminated: " + self.candidates[i].getName() + " (No Votes)")

                #Adds candidate to min array if this is the first candidate checked
                elif(len(min) == 0):
                    min.append(self.candidates[i])

                #Adds candidate to min array if they tie for lowest votes
                elif(self.candidates[i].getVotes(roundNum) == min[0].getVotes(roundNum)):
                    min.append(self.candidates[i])

                #Clears min array and adds candidate if they have a lower number of votes
                elif(self.candidates[i].getVotes(roundNum) < min[0].getVotes(roundNum)):
                    min.clear()
                    min.append(self.candidates[i])

            #Winner is declared if winner array has 1 candidate
            if(len(self.winner) == 1):
                for i in self.candidateNames:
                    if((not (i == self.winner[0].getName())) and (not self.candidates[i].getEliminated())):
                        self.candidates[i].eliminate(roundNum)
                #print("Winner: " + self.winner[0].getName() + " " + str(self.winner[0].getVotePercent(roundNum)))
                self.winner[0].setWinner(roundNum)
                self.rounds = roundNum
                
            else:

                #Eliminates candidates with minimum number of votes 
                if(len(min) < len(self.candidates) - self.numEliminated):
                    for i in min:
                        i.eliminate(roundNum)
                        self.numEliminated += 1
                        #print("Eliminated: " + i.getName() + " " + str(i.getVotePercent(roundNum)))
                    self.runRound(self,filename, roundNum + 1, numSlots)

                #Declares a tie if all candidates would be eliminated due to tie for minimum votes    
                else:
                    #print("Tie:")
                    self.rounds = roundNum
                    for i in self.candidateNames:
                        if(not self.candidates[i].getEliminated()):
                            self.candidates[i].eliminate(roundNum)
                    for i in min:

                        #Adds candidate to winner array
                        self.winner.append(i)
                        i.setTie(roundNum)
                        #print(i.getName())
    
    #Returns a string that represents the round results for a given round number
    def getRoundResult(self, roundNum):
        roundNum -= 1
        results = []
        if(roundNum <= self.rounds):
            returnVal = "Round " + str(roundNum + 1) + "\n"
            #Candidate round result is obtained for each candidate and added to results array
            for i in self.candidateNames:
                results.append(self.candidates[i].getRoundResult(roundNum))
            
            #Round results are sorted to ensure the order is consistent, and to make results look nice
    
            #First, results are sorted alphabetically by name
            #Result is split by commas, and index 0 is selected
            #Results are sorted using this value
            results.sort(key = lambda results: results.split(", ")[0])
                
            #Then, results are sorted by round number at the end of the result
            #Result is split by commas, and index 3 is selected
            #Result is split by colon, and index 1 is selected
            #Results are sorted using this value
            results.sort(key = lambda results: int(results.split(", ")[3].split(": ")[1]))

            #Lastly, results are sorted by number of votes recieved during round
            #Result is split by commas, and index 1 is selected
            #Result is split by whitespace, and index 0 is selected
            #Results are sorted using this value
            results.sort(key = lambda results: int(results.split(", ")[1].split()[0]))
            for i in results:
                returnVal += i + "\n"
            return(returnVal)