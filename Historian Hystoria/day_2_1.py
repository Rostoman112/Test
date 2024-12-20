filename = "input_day_2.txt"
with open(filename, "r") as file:
    reports = file.readlines()

reports = [list(map(int, line.split())) for line in reports]

safe_count = 0

for report in reports:
    is_safe = True
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            is_safe = False
            break

    if is_safe:
        increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
        decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

        if increasing or decreasing:
            safe_count += 1

print(safe_count)
