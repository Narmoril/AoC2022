x = 1
xList = ["_", 1]
result = 0

# part 1

with open("Advent of Code\AoC2022\Day 10\input.txt", "r") as file:
    for line in file:
        if "noop" in line:
            pass
        elif "addx" in line:
            xList.append(x)
            x += int(str(line.strip().split(" ")[1]))
        xList.append(x)

for i in range(20, 221, 40):
    result += xList[i] * i

print("The sum of the six signal strengths is:", result)

# part 2

x = 0

xList[0], xList[1], xList[2], xList[3], xList[4], xList[5] = (
    xList[1:42],
    xList[41:82],
    xList[81:122],
    xList[121:162],
    xList[161:202],
    xList[201:],
)

for i in range(0, 6):
    for k in xList[i]:
        if x in range(int(k) - 1, int(k) + 2) and x < 41:
            xList[i][x] = "#"
            x += 1
        elif x not in range(int(k) - 1, int(k) + 2) and x < 41:
            xList[i][x] = "."
            x += 1
    x = 0

print(
    f"{xList[0]}, \n{xList[1]}, \n{xList[2]}, \n{xList[3]}, \n{xList[4]}, \n{xList[5]}"
)
