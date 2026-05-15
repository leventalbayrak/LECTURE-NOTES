file = open("log.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    parts = line.strip().split(',')
    attacker = parts[0].split(':')[1]
    defender = parts[1].split(':')[1]
    damage = parts[2].split(':')[1]
    print(f"{attacker} attacked {defender} for {damage}")
    