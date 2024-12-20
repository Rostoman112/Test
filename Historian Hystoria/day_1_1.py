from collections import Counter

filename = 'input.txt'
with open(filename, 'r') as file:
    places = file.readlines()

column_1 = []
column_2 = []

for place in places:
    part = place.split()
    column_1.append(int(part[0]))
    column_2.append(int(part[1]))

column_2_sorted = Counter(column_2)

suma = 0

for place in column_1:
    suma += place * column_2_sorted.get(place, 0)

print(suma)
