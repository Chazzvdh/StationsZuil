file1 = open("MyFile.txt", "w")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list:
    if (i % 2) == 0:
        file1.write(str(i))
