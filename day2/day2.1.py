lines = []

with open("day2.in") as input:
    for line in input:
        lines.append(line.rstrip())

reports = []

for line in lines:
    reports.append(list(map(int, line.split())))


safe_total = 0

for report in reports:
    previous = None
    direction = None
    safe = True

    for level in report:
        if previous == None:
            previous = level
            continue

        if level > previous:
            if direction == None:
                direction = "increase"
            
            if direction != "increase":
                safe = False
                continue #unsafe

            if ((level - previous) < 1) or ((level - previous) > 3):
                safe = False
                continue #unsafe

        if level < previous:
            if direction == None:
                direction = "decrease"
            
            if direction != "decrease":
                safe = False
                continue #unsafe

            if ((previous - level) < 1) or ((previous - level) > 3):
                safe = False
                continue #unsafe

        if level == previous:
            safe = False
            continue

        previous = level

    if safe:
        safe_total += 1

print(safe_total)