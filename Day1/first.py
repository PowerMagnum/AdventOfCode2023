with open("input.txt","r") as file:
    data = file.readlines()
#print(data,"\n")   

def first(data):
    tot = 0
    for line in data:
        numbers = []
        for x in line:
            if x.isdigit():
                numbers.append(x)
        #print(numbers)
        tot += int(numbers[0] + numbers[-1])
    return tot

def second(data):
    tot = 0
    for line in data:
        numbers = []
        print(line,end="")
        line = numberilize(line)
        print(line,end="")
        for x in line:
            if x.isdigit():
                numbers.append(x)
        print(numbers,end="\n\n")
        tot += int(numbers[0] + numbers[-1])
    return tot

def numberilize(line: str):
    numbs = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    for text in numbs:    
        x = line.find(text)
        while x > -1:
            line = line[:x+1] + numbs[text] + line[x+2:]
            x = line.find(text)
    return line

print("Q1: ",first(data))
print("Q2: ",second(data))