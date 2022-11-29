
import subprocess

# 2x^4+2x^3+2x+1
# x^4 + 2*x^3 + 0*x^2 + x + 3
F5 = [2, 0, 2, 1]  
F2 = [0, 0, 1, 1] # x^4 + x + 1

resultString = ""
fiveString = ""
working5 = [0, 0, 0, 1]
working2 = [0, 0, 0, 1]

def coolF(numFromFive, numFromTwo):
    return numFromFive *2 + numFromTwo 

def cycle(arr):
    for i in range(3):
        arr[i] = arr[i+1]
    arr[3] = 0
    return arr

for _ in range(10003):
    taken5 = working5[0]
    taken2 = working2[0]
    newNumber = coolF(taken5, taken2)
    resultString += str(newNumber)
    if working2 == [0, 0, 0, 0]:
        working2 = [1, 1, 0, 1]
    elif working2 == [1, 1, 1, 1]: 
        working2 = [0, 0, 0, 0]
    else:
        working2 = cycle(working2)
        for i in range(4):
            working2[i] += taken2 * F2[i]
            working2[i] = working2[i]%2
    if working5 == [0, 0, 0, 0]:
        working5 = [0, 1, 0, 2]
        # 2 1 2 3 for 2x^4+2x^3+2x+1
        # 3 1 2 3 for x^4 + 2*x^3 + 0*x^2 + x + 3
    elif working5 == [1, 1, 1, 1]:
        working5 = [0, 0, 0, 0]
    else:
        working5 = cycle(working5)
        
        for i in range(4):
            working5[i] += (taken5 * F5[i]) * 2  #times three as it is the multiplicative inverse of 2 (the coefficient of x^4)
            working5[i] = working5[i]%5
    print(working5)
    fiveString += str(taken5)

printFile = open("./printFile.txt", "w")
printFile.write(resultString)
printFile = open("./fuckaround.txt", "w")
printFile.write(fiveString)
print(resultString)



    