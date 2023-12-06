with open("example1.txt","r") as file:
    data = file.readlines()

engMat = []
approved = []

def first(data: str):
    for line in data:
        engMat.append(list(line.strip()))
    for x in range(len(engMat)):
        redingNum = False
        approvedNum = False
        for y in range(len(engMat[0])):
            print(engMat[x][y], end="")
            if engMat[x][y].isdigit():
                redingNum = True
                #print("'",end="")
            print("'" if controlSlot(x,y) else "" , end="")
            #print(controlSlot(x, y), end="")
        print()

def controlSlot(x,y):
    esito = False
    for i in range(-1, 2):
        if x + i < 0 or x + i >= len(engMat):
            continue
        for j in range(-1, 2):
            if y + j < 0 or y + j >= len(engMat[0]) or (x == 0 and y == 0):
                continue
            if (not engMat[x][y].isdigit()) and engMat[x][y] != ".":
                esito = True
    return esito


first(data)

