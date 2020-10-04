# read sample.txt and print the number of lines

file1 = open("sample.txt", 'r')
print(len(file1.readlines()))
file1.close()
