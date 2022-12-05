


F5 = [2, 0, 2, 1] # 2x^4+2x^3+2x+1
F2 = [0, 0, 1, 1]  # x^4 + x + 1

resultString = ""
working5 = [0, 0, 0, 0]
working2 = [0, 0, 0, 0]


def coolF(numFromFive, numFromTwo):
    return numFromFive * 2 + numFromTwo


def cycle(arr):
    for i in range(3):
        arr[i] = arr[i+1]
    arr[3] = 0
    return arr


def generateDeBruijn(sequence, field, taken):
    if(sequence == [0, 0, 0, 0]):
        sequence = [0, 0, 0, 1]
    elif(sequence == [1, 0, 0, 1] and field == 2 or
         sequence == [3, 3, 0, 3] and field == 5):
        sequence = [0, 0, 0, 0]
    else:
        sequence = cycle(sequence)
        coeff = 0
        if(field == 2):
            coeff = 1
            poly = F2
        if field == 5:
            coeff = 2
            poly = F5
        for i in range(4):
            sequence[i] += taken * poly[i] * coeff
            sequence[i] = sequence[i] % field
    return sequence


for _ in range(10003):
    taken5 = working5[0]
    taken2 = working2[0]
    newNumber = coolF(taken5, taken2)
    resultString += str(newNumber)
    working2 = generateDeBruijn(working2, 2, taken2)
    working5 = generateDeBruijn(working5, 5, taken5)

printFile = open("./printFile.txt", "w")
printFile.write(resultString)
print(resultString)
