import re

with open("input.txt","r") as file:
    data = file.readlines()


def first(data: str):
    vals = {"red" : 12, "green" : 13, "blue" : 14}
    tot = 0
    for line in data:
        esito = True
        line = line.strip().split(":")
        line[0] = line[0].split()[1]
        line[1] = line[1].split(";")
        for serie in line[1]:
            serie = serie.split(",")
            for slot in serie:
                slot = slot.split()
                if int(slot[0]) > vals[slot[1]]:
                    esito = False
                    break
        if esito:
            tot += int(line[0])
        print(line)
    return tot

def second(data: str):
    tot = 0
    for line in data:
        maxs = {"red" : 0, "green" : 0, "blue" : 0}
        line = line.strip().split(":")
        line[0] = line[0].split()[1]
        line[1] = line[1].split(";")
        for serie in line[1]:
            serie = serie.split(",")
            for slot in serie:
                slot = slot.split()
                if int(slot[0]) > maxs[slot[1]]:
                    maxs[slot[1]] = int(slot[0])
        parz = maxs["red"] * maxs["green"] * maxs["blue"]
        print(line)
        print(parz)
        tot += parz
    return tot

#print("Q1: " , first(data))
print("Q2: ", second(data))