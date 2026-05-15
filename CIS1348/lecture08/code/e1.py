
name = ["gengar", "pikachu", "wailord", "lucario", "bulbasaur"]
health = [100, 100, 300, 100, 100]
reflectdamage = [2.0,0,0.8,0,0]

file = open("log_ids_only.log", "r")
lines = file.readlines()
file.close()

for line in lines:
    parts = line.strip().split('\t')
    attackerid = int(parts[0])
    defenderid = int(parts[1])
    damage = int(parts[2])

    health[defenderid] -= damage
    if reflectdamage[defenderid] > 0:
        health[attackerid] -= damage * reflectdamage[defenderid]
        print("REFLECT!!!")

    print(f"{name[attackerid]} spit on {name[defenderid]} for {damage} water damage")
    print(f"attacker:{health[attackerid]} defender:{health[defenderid]}")