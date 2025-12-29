filename = "example.txt"

# read()
f = open(filename, "r")
print(f.read())
f.close()

# readline()
f = open(filename, "r")
print(f.readline())
f.close()

# readlines()
f = open(filename, "r")
print(f.readlines())
f.close()

# with open()
with open(filename, "r") as f:
    for line in f:
        print(line)
