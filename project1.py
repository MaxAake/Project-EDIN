
from math import floor, sqrt, gcd
import subprocess


N = 89692892892645583511288289
Nsmall = 114450059
def findR(N, L): 
    F = findPrimes(L + 5)
    triedNums = set()
    computedNums = []
    factorList = []
    rModList = []
    j = 1
    k = 1
    while(len(triedNums) < L - 5):
        r = floor(sqrt(k*N) + j)
        rMod = (r**2)%N
        [works, factors] = factor(rMod, F)
        computedNum = 1
        for fac in factors:
            computedNum = computedNum * fac
        if(works == True and (computedNum not in triedNums)):
            triedNums.add(computedNum)
            computedNums.append(computedNum)
            factorList.append([r, factors])
            rModList.append(rMod)
        j += 1
        if(j == 100):
            k += 1
            j = 0
    file1 = open("MyFile.txt", "w")
    file1.write(str(L-5) + " " + str(L+5) + "\n")
    for factors in factorList:
        string = ""
        counter = 0
        nextprime = factors[1][0]
        for prime in F:
            if prime == nextprime and counter < len(factors[1]):
                string += "1 "
                counter += 1
                if counter < len(factors[1]):
                    nextprime = factors[1][counter]
            else:
                string += "0 "
        string += "\n"
        file1.write(string)
    subprocess.call(["GaussBin.exe", "MyFile.txt", "outFile.txt"])
    file2 = open("outFile.txt", "r")
    lines = file2.readlines()
    for line in lines[1 : len(lines)]:
        characters = line.split()
        prodX = 1
        prodY = 1
        for i in range(0, len(characters)-1):
            if characters[i] == "1":
                prodY = prodY * computedNums[i]
                prodX = prodX * rModList[i]
        tryFactor = gcd(prodY - prodX, N)
        if tryFactor != 1:
            print("Possible factor: " + str(tryFactor) + "\n Other factor would be: " + str(N/tryFactor) + " remainder: " + str(N%tryFactor))
            break
        
def factor(rMod, smoothPrimes):
    factors = []
    for prime in smoothPrimes:
        temp = 0
        while(rMod % prime == 0):
            rMod = rMod/prime
            temp += 1
        if(temp % 2 == 1):
            factors.append(prime)
    if(rMod != 1 or len(factors) < 2):
        return [False, []]
    else:
        return [True, factors]

def findPrimes(L):
    primes = [2]
    i = 3
    while(len(primes) < L):
        prime = True
        for j in primes:
            if(i % j == 0):
                prime = False
        if prime:
            primes.append(i)
        i += 2
    return primes
    
findR(testNum, 1000)