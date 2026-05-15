import random

for i in range(4):
    file = open(f"pokemon{i}.txt", "r")
    name = file.readline().strip()[1:-1]
    file.close()
    print(name)

for i in range(100000):
    file = open(f"spagett_{i}.exe", "w")

    filesize = random.randint(100,1000000)
    for j in range(filesize):
        c = chr( ord('a') + random.randint(0,25) )
        if c == 'y':
            file.write('\n')
        else:
            file.write(c)
    
    file.close()
