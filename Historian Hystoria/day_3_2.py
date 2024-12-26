import re

filename = "input_day_3.txt"

with open(filename, "r") as file:
    data = file.readlines()

data_string = ' '.join(data)

pattern_mul = r"(?<=do.*)(mul(\d+,\d+\))"

pattern_do = r"do\(\)"

pattern_dont = r"don\'t\(\)"

result = re.findall(pattern_mul, data_string)
