import csv

class Party:
    def __init__(self, name, votesNum, originalSeat) -> None:
        self.name = name[::-1]
        self.votes = int(votesNum.replace(',', ''))
        self.seats = int(originalSeat)
        self.newSeats = 0


def jeffersonsF(s):
    return s+1

def webstersF(s):
    return s+0.5

def generalF(s, y):
    return s+1-y

def initializePartiesFromFile(filename) -> list:
    parties = list()
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            parties.append(Party(row[0], row[1], row[2]))
    return parties

if __name__ == "__main__":
    # Initialize a list for parties
    parties = initializePartiesFromFile('results.csv')

    # Initialize a list for quotient results
    quotient = list()
    for party in parties:
        quotient.append(0)

    # For each Seat calculate a quotient for each party and add one Seat for a party with the highest quotient
    # for i in range(0,120):
    #     for index, party in enumerate(parties):
    #         quotient[index] = party.votes/webstersF(party.newSeats)

    #     max_index = quotient.index(max(quotient))
    #     parties[max_index].newSeats += 1

    # print("\t"+"party name", "\t","new/","\t", "old seats")
    # for party in parties:
    #     print("\t"+party.name, "\t",party.newSeats,"\t", party.seats)

    j = 0.001
    different = True
    while different and j != 1:
        for i in range(0,120):
            for index, party in enumerate(parties):
                quotient[index] = party.votes/generalF(party.newSeats, j)

            max_index = quotient.index(max(quotient))
            parties[max_index].newSeats += 1
        j = j + 0.001
        for party in parties:
            if party.seats != party.newSeats:
                different = False
            party.newSeats = 0

    y = 1-j
    print(y)






