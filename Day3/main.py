with open("input.txt","r") as file:
    data = file.readlines()

engMat = []
approved = []

def first(data: str):
    tot = 0
    for line in data:
        engMat.append(list(line.strip()))
    for x in range(len(engMat)):
        readingNum = False
        approvedNum = False
        numCache = ""
        for y in range(len(engMat[0])):
            print(engMat[x][y], end="")
            if engMat[x][y].isdigit():
                readingNum = True
                if controlSlot(x,y):
                    approvedNum = True
                numCache += engMat[x][y]
            elif readingNum and approvedNum:
                readingNum = False
                approvedNum = False
                approved.append(numCache)
                numCache = ""
                #print("'",end="")
            else:
                numCache = ""
            #controlSlot(x,y)
            #print("'" if controlSlot(x,y) and engMat[x][y].isdigit() else "-" , end="")
            #print(controlSlot(x, y), end="")
        print()
    for k in approved:
        tot += int(k)
    print(approved)
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
                #print("  Y:  "+engMat[x+i][y+j])
            #else:
                #print("  -:  "+engMat[x+i][y+j])
    #print(esito)
    return esito


print(first(data))


