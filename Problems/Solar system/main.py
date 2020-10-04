# create the planets.txt

solar = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n']
file1 = open("planets.txt", 'w', encoding='utf-8')
file1.writelines(solar)
file1.close()
