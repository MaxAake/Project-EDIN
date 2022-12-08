from numpy import *
import matplotlib.pyplot as plt

#LFSR sequence polynomials C(D) for the three different LFSRs:
# C13 = D^13 + D^11 + D^10 + D^7 + D^6 + D^4 + D^2 + D + 1
C13 = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
# C15 = D^15 + D^13 + D^11 + D^10 + D^7 + D^6 + D^4 + D^2 + 1
C15 = [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
# C17 = D^17 + D^16 + D^13 + D^10 + D^8 + D^5 + D^4 + D^2 + 1
C17 = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1] 
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
    ##print(resultString)
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
    seqs = []
    for i in range(length):
        seq += [0]
    peace = []
    for i in range(2**length):
        seq1 = GetSequence(C, seq)
        peace += [similarity(seq1, trueSeq)]
        seqs += [seq1]
        seq[length-1] += 1
        for i in range(length):
            if seq[length-1-i] == 2:
                if length-1-i != 0:
                    seq[length-2-i] += 1
                seq[length-1-i] = 0
            else:
                break
    return [peace, seqs]


P13 = testSequences(C13, 13)
P15 = testSequences(C15, 15)
P17 = testSequences(C17, 17)
maxVal3 = 0
maxSeq3 = []

# Returns the index of the list element with the largest deviation from 0.5.
def getHighestIndex(listOfSequences):
    highestDeviation = 0
    for i in range(len(listOfSequences[0])):
        val = listOfSequences[0][i]
        val = abs(val - 0.5)
        if(val > highestDeviation):
            highestDeviation = val
            index = i
    return index

maxSeq1 = P13[1][getHighestIndex(P13)]
maxSeq2 = P15[1][getHighestIndex(P15)]
maxSeq3 = P17[1][getHighestIndex(P17)]

def majorityFunction(s, t, r):
    resultstring = ""
    for i in range(len(s)):
        ones = 0
        if s[i] == "1":
            ones += 1
        if t[i] == "1":
            ones += 1
        if r[i] == "1":
            ones += 1
        if ones > 1:
            resultstring += "1"
        else:
            resultstring += "0"
    return resultstring
print(maxSeq1)
print(maxSeq2)
print(maxSeq3)
endResult = majorityFunction(maxSeq1, maxSeq2, maxSeq3)
#print(P13)
#print(P15)
print(endResult)
print(trueSeq)
plt.plot(P13[0])
plt.show()
plt.plot(P15[0])
plt.show()
plt.plot(P17[0])
plt.show()