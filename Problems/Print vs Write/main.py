numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file1 = open('file_with_list.txt', 'w')
print(numbers, file=file1, end='')
file1.close()
