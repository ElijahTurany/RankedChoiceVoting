import csv

class BallotProccessor:
    def loadBallots(filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(f'\t{row[0]}, {row[1]}, {row[2]}')



BP = BallotProccessor

BP.loadBallots("SmallListBallots.csv")