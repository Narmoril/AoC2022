priority_sum = 0

# part 1

with open("input.txt", "r") as file:
    for line in file:
        contents = line
        first_half = contents[:len(line)//2]
        second_half = contents[len(line)//2:]

        for x in first_half:
            if x in second_half:
                if (ord(x) >= 65) and (ord(x) <= 90):
                    priority_sum += ord(x) - 38
                    break
                elif (ord(x) >= 97) and (ord(x) <= 122):
                    priority_sum += ord(x) - 96
                    break

print("The sum of the requested priorities is ", priority_sum, ".", sep = "")

# part 2

priority_sum = 0
group_counter = 0
lineList = []

with open("input.txt", "r") as file:
    for line in file:
        lineList.append(line)
        if group_counter == 2:
            for x in lineList[0]:
                if (x in lineList[1]) and (x in lineList[2]): # made a mistake here, wrote 'x in a[1] and a[2]' (the latter of which is always true here)
                    if (ord(x) >= 65) and (ord(x) <= 90):
                        priority_sum += ord(x) - 38
                        break
                    elif (ord(x) >= 97) and (ord(x) <= 122):
                        priority_sum += ord(x) - 96
                        break
            lineList = []
            group_counter = 0
        elif group_counter < 2:
            group_counter += 1

print("The sum of the elves' group badges is ", priority_sum, ".", sep = "")