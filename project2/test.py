with open  ('PROJ2-HNS.txt', 'r') as domains:
    lines = domains.read().splitlines()
    for line in lines:
        print(line)

print("*****")

with open ('PROJ2-HNS.txt', 'r') as domains:
    lines = domains.readlines()
    
    for line in lines:
        print(line)
