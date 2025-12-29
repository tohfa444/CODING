outputFile = open("UpdatedFile.txt", "w")

inputFile = open("Codingal.txt", "r")

lssf = set()

for line in inputFile:

    if line not in lssf:
        outputFile.write(line)
        lssf.add(line)

inputFile.close()
outputFile.close()

    