filename = "data.txt"

# Write mode (w)
f = open(filename, "w")
f.write("Hello World\n")
f.close()

# Append mode (a)
f = open(filename, "a")
f.write("Learning Python File Handling\n")
f.close()

# Read mode (r)
f = open(filename, "r")
print(f.read())
f.close()

# Read & Write mode (r+)
f = open(filename, "r+")
f.write("Start\n")
f.seek(0)
print(f.read())
f.close()
