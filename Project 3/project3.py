from numpy import *
import matplotlib.pyplot as plt

#LFSR sequence polynomials C(D) for the three different LFSRs:
# C1 = D^13 + D^11 + D^10 + D^7 + D^6 + D^4 + D^2 + D + 1
C1 = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1] 
# C2 = D^15 + D^13 + D^11 + D^10 + D^7 + D^6 + D^4 + D^2 + 1
C2 = [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
# C3 = D^17 + D^16 + D^13 + D^10 + D^8 + D^5 + D^4 + D^2 + 1
C3 = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
# The sequence group 02 was given was:
trueSeq = "0111101011011110011101000010111011001110110101101110001000101110110111101011001011110000111011110110001000010110010111111011110011000001101111100100011110111001110011000010100011001110010110111"

def GetSequence(poly, initialState):
    resultString = ""
    state = initialState.copy()
    for i in range(len(trueSeq)):
        resultString += str(state[len(state) - 1])
        newNum = 0
        for i in range(len(state)):
            newNum += state[i] * poly[i]
        for i in range(1, len(state)):
            state[len(state) - i] = state[len(state) - i - 1]
        newNum = newNum % 2
        state[0] = newNum
    print(resultString)
    return resultString


# It is assumed here that seq1 and seq2 are of the same length, otherwise throws out of bounds. 
# Gets the similarity of two sequences.
def similarity(seq1, seq2):
    sameValues = 0
    size = len(seq1)
    for i in range(size):
        if seq1[i] == seq2[i]:
            sameValues += 1
    return sameValues / size

def testSequences(C, length):
    seq = []
    for i in range(length):
        seq += [0]
    peace = []
    for i in range(2**length):
        seq1 = GetSequence(C, seq)
        peace += [similarity(seq1, trueSeq)]
        seq[length-1] += 1
        for i in range(length):
            if seq[length-1-i] == 2:
                if length-1-i != 0:
                    seq[length-2-i] += 1
                seq[length-1-i] = 0
            else:
                break
    return peace


#P1 = testSequences(C1, 13)
#P2 = testSequences(C2, 15)
P3 = testSequences(C3, 17)

P = P3
maxVal = 0
for i in range(len(P)):
    P[i] = abs(P[i]-0.5)
    if P[i] > maxVal:
        maxVal = P[i]
#print(maxVal)
print(P)
#print(P2)
#print(P3)
plt.plot(P)
plt.show()