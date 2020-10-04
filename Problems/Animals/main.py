# read animals.txt
# and write animals_new.txt

open("animals_new.txt", "w").writelines([animal.replace("\n", " ") for animal in open("animals.txt", "r").readlines()])
