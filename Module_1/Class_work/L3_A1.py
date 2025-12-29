with open("Codingal.txt","w") as file:
    file.write("Hi, I am Penguien and I am 1 year old")
    file.write("Hi I am Penguin")

with open("Codingal.txt", "r") as file:
    data = file.readlines()
    print(data) 
    print("Words in this file are....")
    for line in data:
        print(line)
        word = line.split()
        print(word)