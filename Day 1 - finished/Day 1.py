calories = []
tmp = 0

# part 1

with open("input.txt", "r") as file:
    for line in file:
        if line.strip() != "":
            tmp += int(line)
        else:
            calories.append(tmp)
            tmp = 0
    calories.append(tmp)
print("The maximum amount of calories is ", max(calories), ".", sep="")

# part 2

top3 = [0,0,0]
tmp = 0

with open("input.txt", "r") as file:
    for line in file:
        if line.strip() != "":
            tmp += int(line)
        else:
            if top3[0] < tmp:
                 top3[2] = top3[1]
                 top3[1] = top3[0]
                 top3[0] = tmp
            elif top3[0] < tmp:
                 top3[2] = top3[1]
                 top3[1] = tmp
            elif top3[2] < tmp:
                 top3[2] = tmp
            tmp = 0
    if top3[0] < tmp:
         top3[2] = top3[1]
         top3[1] = top3[0]
         top3[0] = tmp
    elif top3[0] < tmp:
         top3[2] = top3[1]
         top3[1] = tmp
    elif top3[2] < tmp:
         top3[2] = tmp

print("The calorie amount of the top three elves is ", (top3[0] + top3[1] + top3[2]), "calories.", sep="")