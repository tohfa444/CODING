with open("Codingal.txt") as fp:
    data1 = fp.read()

with open("sample_doc.txt") as fp:
    data2 = fp.read()

data1 = data1 + "\n"
data3 = data1 + data2

print("Merring two files....")
with open("MergedFile.txt", "w") as fp:
    fp.write(data3)