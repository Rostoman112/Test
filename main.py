filename = 'input.txt'
with open(filename, 'r') as file:
    places = file.readlines()

column_1 = []
column_2 = []

for place in places:
    part = place.split()
    column_1.append(int(part[0]))
    column_2.append(int(part[1]))

column_1.sort()
column_2.sort()

suma = 0

for c1, c2 in zip(column_1, column_2):
    suma += abs(c1 - c2)

print(suma)
