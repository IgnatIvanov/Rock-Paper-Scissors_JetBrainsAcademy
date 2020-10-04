with open('salary.txt', 'r') as f1, open('salary_year.txt', 'w') as f2:
    f2.writelines(str(int(x) * 12) + '\n' for x in f1.readlines())
