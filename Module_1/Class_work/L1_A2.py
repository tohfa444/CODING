fileread = open("Codingal.txt", "r")
print(fileread.read())
fileread.close()

filewrite = open("Codingal.tx6t", "w")
filewrite.write("File in write mode...")
filewrite.write("Hi! I am Penguin. I am 1 year old")
filewrite.close()

file_append = open("Codingal.txt", "a")
file_append.write("\nFile in append mode...")
file_append.write("Hi! I am Penguin. I am 1 year old")
file_append.close()