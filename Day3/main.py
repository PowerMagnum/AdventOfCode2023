from colorama import Fore, Back
with open("input.txt","r") as file:
    data = file.readlines()

engMat = []
approved = []
simboli = set()
notApproved = []

stars = {}

for line in data:
    engMat.append(list(line.strip()))

def first(data: str):
    readingNum = False
    approvedNum = False
    numCache = ""
    tot = 0
    for x in range(len(engMat)):
        for y in range(len(engMat[0])):
            col = Back.BLACK
            #print(engMat[x][y], end="")
            if engMat[x][y].isdigit():
                readingNum = True
                if controlSlot(x,y):
                    approvedNum = True
                numCache += engMat[x][y]
            elif readingNum and approvedNum:
                readingNum = False
                approvedNum = False
                approved.append(numCache)
                tot += int(numCache)
                numCache = ""
                #print("'",end="")
            elif readingNum:
                if numCache != "":
                    notApproved.append(numCache)
                    numCache = ""
                    col = Back.RED
            else:
                numCache = ""
                readingNum = False
            #controlSlot(x,y)
            #print("'" if controlSlot(x,y) and engMat[x][y].isdigit() else "-" , end="")
            #print(controlSlot(x, y), end="")+
            #print(col + engMat[x][y], end="")
        #print()
    #for k in approved:
        #tot += int(k)
    #print(approved)
    return tot

def controlSlot(x,y):
    esito = False
    #print(f"[{engMat[x][y]}]  x:{x} y:{y}")
    for i in range(-1, 2):
        #print(f"x-shift:{i}")
        if x + i < 0 or x + i >= len(engMat):
            #print("  pass")
            continue
        for j in range(-1, 2):
            #print(f"   y-shift:{j}",end="")
            if y + j < 0 or y + j >= len(engMat[0]) or (i == 0 and j == 0):
                #print("\n     pass")
                continue
            if (not engMat[x+i][y+j].isdigit()) and engMat[x+i][y+j] != ".":
                esito = True
                simboli.add(engMat[x+i][y+j])
                #print("  Y:  "+engMat[x+i][y+j])
            #else:
                #print("  -:  "+engMat[x+i][y+j])
    #print(esito)
    return esito

def second(data: str):
    readingNum = False
    approvedNum = False
    numCache = ""
    bindCoords = ""
    tot = 0
    for x in range(len(engMat)):
        for y in range(len(engMat[0])):
            col = Back.BLACK
            #print(engMat[x][y], end="")
            if engMat[x][y].isdigit():
                readingNum = True
                check = controlSlotStar(x,y)
                if check:
                    bindCoords = check
                    approvedNum = True
                numCache += engMat[x][y]
            elif readingNum and approvedNum:
                readingNum = False
                approvedNum = False
                approved.append(numCache)
                if bindCoords not in stars.keys():
                    stars[bindCoords] = [numCache]
                else:
                    stars[bindCoords].append(numCache)
                numCache = ""
                #print("'",end="")
            elif readingNum:
                if numCache != "":
                    notApproved.append(numCache)
                    numCache = ""
                    col = Back.RED
            else:
                numCache = ""
                readingNum = False
    for coord in stars.keys():
        if len(stars[coord]) == 2:
            tot += int(stars[coord][0]) * int(stars[coord][1])
            #print(stars[coord])
    return tot

def controlSlotStar(x,y):
    for i in range(-1, 2):
        if x + i < 0 or x + i >= len(engMat):
            continue
        for j in range(-1, 2):
            if y + j < 0 or y + j >= len(engMat[0]) or (i == 0 and j == 0):
                continue
            if engMat[x+i][y+j] == "*":
                return f"{x+i}_{y+j}"
    return False


print("Q1: ",first(data))
print("Q2: ", second(data))
#print(stars)
#print(approved)
#print()
#print(simboli)
#print(notApproved)
