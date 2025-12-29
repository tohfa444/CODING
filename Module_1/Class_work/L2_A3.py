f1 = open("Codingal.txt", "r")
f2 = open("CodingalUpdated.txt", "w")

for line in f1.readlines():

    if not (line.startwith("Coding")):
        print(line)
        f2.write(line)

f1.close()
f1.close()