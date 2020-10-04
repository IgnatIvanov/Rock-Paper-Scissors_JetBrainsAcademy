# write your code here
for i in range(1, 11):
    file_name = "file" + str(i) + ".txt"
    with open(file_name, 'w') as file:
        file.write(str(i))
