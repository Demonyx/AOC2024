lines = []

with open("day1.in") as input:
    for line in input:
        lines.append(line.rstrip())

list1 = []
list2 = []

for line in lines:
    raw = list(line.split())
    list1.append(int(raw[0]))
    list2.append(int(raw[1]))

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)