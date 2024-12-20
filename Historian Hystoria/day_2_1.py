filename = 'input_day_2.txt'
with open(filename, "r") as file:
    reports = file.readlines()

for report in reports:
    for number in report:
        