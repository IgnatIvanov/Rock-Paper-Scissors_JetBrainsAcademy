# read sums.txt

file1 = open('sums.txt', 'r')

for line in file1:
    args = (line.split(" "))
    print(int(args[0]) + int(args[1]))

file1.close()
