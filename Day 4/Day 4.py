numbers = [0, 0, 0, 0]
elf1counter = 0
elf2counter = 0
tmpList = []
final_counter1 = 0
final_counter2 = 0
counter = 0

# part 1
# I'm sure this code could be at least half as long and have half as many variables, but hey, at least it works

with open("Advent of Code\\AoC2022\Day 4\input.txt", "r") as file:
    for line in file:
        for x in line.strip() + ",":
            if x.isdigit():
                tmpList.append(x)
            elif x.isdigit() == False:
                numbers[counter] = int("".join(tmpList))
                tmpList = []
                counter += 1
        counter = 0
        elf1counter, elf2counter = numbers[0], numbers[2]
        if ((numbers[0] <= numbers[2]) and (numbers[1] >= numbers[3])) or (
            (numbers[2] <= numbers[0]) and (numbers[3] >= numbers[1])
        ):
            final_counter1 += 1
        if (  # the if function contains part 2's code
            (numbers[2] <= numbers[0] <= numbers[3])
            or (numbers[2] <= numbers[1] <= numbers[3])
            or (numbers[0] <= numbers[2] <= numbers[1])
        ):
            final_counter2 += 1
        numbers = [0, 0, 0, 0]
        line.split(",")[1][2]

print("The count for highly unnecessary resource distribution is :", final_counter1)

print("The count for unnecessary resource distribution is :", final_counter2)
