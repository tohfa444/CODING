file = open("Codingal.txt", "r")
counter = 0

content = file.read()

colist = content.split("\n")
print(colist)

for i in colist:
    if i:
        counter += 1 

print(counter)