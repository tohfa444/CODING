# Write to a file
with open("data.txt", "w") as f:
    f.write("Hello Python\nWelcome to file handling")

# Read the file
with open("data.txt", "r") as f:
    print(f.read())

# Append to the file
with open("data.txt", "a") as f:
    f.write("\nThis line is added later")
