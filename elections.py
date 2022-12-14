import csv

class Party:
    def __init__(self, name, votesNum, originalSeat, newSeats = 0, originalPartiesTuple: tuple=None) -> None:
        self.name = name[::-1] # reverse hebrew string
        if isinstance(votesNum, str):
            self.votes = int(votesNum.replace(',', ''))
        else:
            self.votes = votesNum
        self.seats = int(originalSeat)
        self.newSeats = newSeats
        self.originalParties = originalPartiesTuple
    
    def __add__(self, other):
        resultParty = Party(self.name+"+"+other.name, self.votes+other.votes, 0, self.newSeats+other.newSeats, (self, other))
        return resultParty


def jeffersonsF(s, none):
    return s+1

def webstersF(s, none):
    return s+0.5

def generalF(s, y):
    return s+1-y

def initializePartiesFromFile(filename) -> list:
    """creates a list of Party according to a csv file"""
    parties = list()
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            parties.append(Party(row[0], row[1], row[2]))
    return parties

def sumGoodVotes(parties: list) -> int:
    """returns a sum of good votes in this election (Gets a party list)"""
    sum = 0
    for party in parties:
        sum += party.votes
    return sum

def apportionmentAlgorithm(start:int, end:int, methodFunction: callable, parties:list, y=None):
    """
    uses hamiltons method: (party votes)/f(party current seats)
    for each iteration gives one seat to the party the maximizes (party votes)/f(party current seats)
    f is parameter 'methodFunction'
    """
    quotient = list()
    for party in parties:
        quotient.append(0)

    for i in range(start, end):
        for index, party in enumerate(parties):
            quotient[index] = party.votes/methodFunction(party.newSeats,y)
        max_index = quotient.index(max(quotient))
        parties[max_index].newSeats += 1

def electionsAlgorithm(parties: list, seats: int = 120) -> int:
    """
    allocate seats to each party according to the amount of good votes divided by the amount of seats (rounded down)
    returns the amount of unalloccated seats (due to rounding)
    """
    seatCostInVotes = int(sumGoodVotes(parties=parties)/seats)
    allocatedSeats = 0
    for party in parties:
        party.newSeats = int(party.votes/seatCostInVotes)
        allocatedSeats += party.newSeats
    return allocatedSeats