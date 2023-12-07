with open("input.txt","r") as f:
    data = f.read()
    data = data.split("\n\n")

def first(data):
    seeds = [] #D0
    seedToSoil = {} #D1
    soilToFert = {} #D2
    fertToWater = {} #D3
    waterToLight = {} #D4
    lightToTemp = {} #D5
    tempToHum = {} #D6
    humToLoc = {} #D7
    locations = []

    print("Seeds...")
    seeds = data[0].split(":")[1].split()
    print("step1...")
    for line in data[1].split("\n")[1:]:
        print(line)
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            seedToSoil[int(line[1]) + i] = int(line[1]) + i + diff
    print("step2...")
    for line in data[2].split("\n")[1:]:
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            soilToFert[int(line[1]) + i] = int(line[1]) + i + diff
    print("step3...")
    for line in data[3].split("\n")[1:]:
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            fertToWater[int(line[1]) + i] = int(line[1]) + i + diff
    print("step4...")
    for line in data[4].split("\n")[1:]:
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            waterToLight[int(line[1]) + i] = int(line[1]) + i + diff
    print("step5...")
    for line in data[5].split("\n")[1:]:
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            lightToTemp[int(line[1]) + i] = int(line[1]) + i + diff
    print("step6...")
    for line in data[6].split("\n")[1:]:
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            tempToHum[int(line[1]) + i] = int(line[1]) + i + diff
    print("step7...")
    for line in data[7].split("\n")[1:]:
        line = line.split()
        diff = int(line[0]) - int(line[1])
        for i in range(int(line[2])):
            humToLoc[int(line[1]) + i] = int(line[1]) + i + diff
    print("Last...")
    for seed in seeds:
        seed = int(seed)
        step1 = seedToSoil[seed] if seed in seedToSoil else seed
        step2 = soilToFert[step1] if step1 in soilToFert else step1
        step3 = fertToWater[step2] if step2 in fertToWater else step2
        step4 = waterToLight[step3] if step3 in waterToLight else step3
        step5 = lightToTemp[step4] if step4 in lightToTemp else step4
        step6 = tempToHum[step5] if step5 in tempToHum else step5
        step7 = humToLoc[step6] if step6 in humToLoc else step6
        locations.append(step7)
    return min(locations)
    #for x in data:
     #   print("#", x)
print(first(data))

