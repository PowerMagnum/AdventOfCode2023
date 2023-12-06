with open("example1.txt","r") as file:
    data = file.readlines()

def first(data:str):
    tot = 0
    for line in data:
        v_line = 0
        line = line.strip().split(":")[1]
        winners, mine = line.split("|")
        winners = winners.split()
        mine = mine.split()
        #print(winners)
        #print(mine)

        for val in winners:
            if val in mine:
                v_line = 1 if (not int(v_line)) else int(v_line)*2
                print(f"[{val}] -> {v_line}") 
        tot += int(v_line)
    return tot

def second(data):
    toDo = [1 for _ in range(len(data))]
    for l in range(len(data)):
        v_line = 0
        data[l] = data[l].strip().split(":")[1]
        winners, mine = data[l].split("|")
        winners = winners.split()
        mine = mine.split()
        for val in winners:
            if val in mine:
                v_line = 1 if (not int(v_line)) else int(v_line)*2
                print(f"[{val}] -> {v_line}") 
        for k in range(toDo[data.index(data[l])]):
            for i in range(v_line):
                print(l, " ", i)
                toDo[l + i] += 1 
    print(toDo)  
    #return tot

#print(first(data))
second(data)
