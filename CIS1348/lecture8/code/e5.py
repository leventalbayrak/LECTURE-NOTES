
names = [0]*4

for i in range(4):
    file = open(f"pokemon{i}.txt", "r")
    name = file.readline().strip()[1:-1]
    file.close()
    names[i] = name

file = open("log_ids_only.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    parts = line.strip().split('\t')
    attackerid = int(parts[0])
    defenderid = int(parts[1])
    damage = int(parts[2])

    print(f"{names[attackerid]} spit on {names[defenderid]} for {damage} water damage")