import re

filename = "input_day_3.txt"
with open(filename, "r") as file:
    data = file.readlines()

data_string = ' '.join(data)

pattern = r"mul\((\d+),(\d+)\)"

result = re.findall(pattern, data_string)

print(result)

suma = 0

for pair in result:
    num1, num2 = int(pair[0]), int(pair[1])
    suma += num1 * num2


print(suma)
