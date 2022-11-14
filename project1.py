
from math import floor, sqrt


N = 89692892892645583511288289

def findR(N, L): 
    F = findPrimes(L)
    smoothPrimes = []
    for prime in F:
        if prime < L-5:
            smoothPrimes.append(prime)
    print(F)
    triedNums = set()
    factorList = []
    j = 1
    k = 1
    while(len(triedNums) < L - 5):
        r = floor(sqrt(k*N) + j)
        rMod = r%N
        [works, factors] = factor(rMod, smoothPrimes)
        if(works & (rMod not in triedNums)):
            triedNums.add(rMod)
            factorList.append(factors)
            print(len(factorList))
        j += 1
        if(j == 100):
            k += 1
            j = 0
    print(factorList)
        
            
            

def factor(rMod, smoothPrimes):
    factors = []
    for prime in smoothPrimes:
        temp = 0
        while(rMod % prime == 0):
            rMod = rMod/prime
            temp += 1
        if(temp % 2 == 1):
            factors.append(prime)
    if(rMod != 1):
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
    
findR(N, 1000)