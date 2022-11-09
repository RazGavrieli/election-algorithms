import csv

class Party:
    def __init__(self, name, votesNum, originalSeat) -> None:
        self.name = name[::-1]
        self.votes = int(votesNum.replace(',', ''))
        self.seats = originalSeat
        self.newSeats = 0


def jeffersonsF(s):
    return s+1

def webstersF(s):
    return s+0.5

def adamsF(s):
    return s+0.0000001

if __name__ == "__main__":
    print("jefferson results:")
    # Initialize a list for parties
    parties = list()
    with open('results.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            parties.append(Party(row[0], row[1], row[2]))

    # Initialize a list for quotient results
    quotient = list()
    for party in parties:
        quotient.append(0)

    # For each Seat calculate a quotient for each party and add one Seat for a party with the highest quotient
    for i in range(0,120):
        for index, party in enumerate(parties):
            quotient[index] = party.votes/webstersF(party.newSeats)

        max_index = quotient.index(max(quotient))
        parties[max_index].newSeats += 1

    print("\t"+"party name", "\t","new/","\t", "old seats")
    for party in parties:
        print("\t"+party.name, "\t",party.newSeats,"\t", party.seats)



