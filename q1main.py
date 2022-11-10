from elections import *

parties = initializePartiesFromFile('results.csv')
j=0.5
if j == 0:
    print("jeffersons f(s) = s +", str(1-j))
elif j == 0.5:
    print("websters f(s) = s +", str(1-j))
else:
    print("calculating for f(s) = s +", str(1-j))

# create combinedParties for agreed upon deals between parties prior to elections:
combinedParties = list()
combinedParties.append(parties[0]+parties[2]) # likud + bengvir
combinedParties.append(parties[1]+parties[3]) # yesh atid + ganz
combinedParties.append(parties[4]+parties[5]) # shas + tora
combinedParties.append(parties[6])
combinedParties.append(parties[7])
combinedParties.append(parties[8])
combinedParties.append(parties[9])

# First, allocate seats and return the amount of unallocated seats    
allocatedSeats = electionsAlgorithm(parties=combinedParties)

# For each unallocated seats, run an algorithm to allocate the seats according to a method functuin
apportionmentAlgorithm(start=allocatedSeats, end=120, methodFunction=generalF, parties=combinedParties, y=j)

# for each combined partj, divide the seats according to the same algorithm we used for all the parties together
for party in combinedParties:
    if party.originalParties is not None:
        newPartyList = list(party.originalParties)
        a = electionsAlgorithm(parties=newPartyList, seats=party.newSeats)
        apportionmentAlgorithm(start=a, end=party.newSeats, methodFunction=generalF, parties=newPartyList,y=j)


print("\t"+"          ", "\t| S E A T S |")
print("\t"+"party name", "\t","new","\t", "IRL")
for party in parties:
    print("\t"+party.name, "\t",party.newSeats,"\t", party.seats)