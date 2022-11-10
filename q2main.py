from elections import *

if __name__ == "__main__":
    differenceFound = False
    j = 0
    jump = 0.5
    precisionFactor = 0.00001
    # Initialize a list for parties from a .csv file
    parties = initializePartiesFromFile('results.csv')
    while True:
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
        
        # Check if there is a difference between IRL results to current results
        for party in parties:
            if party.seats != party.newSeats: 
                differenceFound = True

        # if we found a difference decrease j by jump, else increase j by jump        
        if not differenceFound:
            j += jump
        else:
            j -= jump
        jump /= 2
        if jump < precisionFactor: 
            break
        differenceFound = False
    # 
    # PRINT RESULTS    
    print("\t"+"          ", "\t| S E A T S |")
    print("\t"+"party name", "\t","seats new","\t", "seats IRL")
    for party in parties:
        print("\t"+party.name, "\t",party.newSeats,"\t", party.seats)
    y = 1-j
    print(y)








