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

similarity_score = 0

for num in list1:
    frequency = 0
    for other_num in list2:
        if other_num > num:
            break
        
        if other_num == num:
            frequency += 1

    similarity_score += num * frequency

print(similarity_score)
