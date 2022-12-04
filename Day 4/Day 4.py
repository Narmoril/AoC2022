numbers = [0,0,0,0]
elf1counter = 0
elf2counter = 0
tmpList = []
first_elf = []
second_elf = []
digits = ["0","1","2","3","4","5","6","7","8","9"]
final_counter = 0
counter = 0

# part 1
# I'm sure this code could be at least half as long and have half as many variables, but hey, at least it works

with open ("input.txt", "r") as file:
    for line in file:
        for x in (line.strip() + ","):
            if x in digits:
                tmpList.append(x)
            elif x not in digits:
                numbers[counter] = int("".join(tmpList))
                tmpList = []
                counter += 1
        counter = 0
        elf1counter, elf2counter = numbers[0], numbers[2]
        while numbers[0] <= numbers[1]:
            first_elf.append(numbers[0])
            numbers[0] += 1
        while numbers[2] <= numbers[3]:
            second_elf.append(numbers[2])
            numbers[2] += 1
        if ((elf2counter in first_elf) and (numbers[3] in first_elf)) or ((elf1counter in second_elf) and (numbers[1] in second_elf)):
            final_counter += 1
        numbers = [0,0,0,0]
        first_elf = []
        second_elf = []

print ("The count for highly unnecessary resource distribution is :", final_counter)

# part 2
# recycled part 1 almost entirely, only exchanged 'and' statements for 'or' statements

final_counter = 0

with open ("input.txt", "r") as file:
    for line in file:
        for x in (line.strip() + ","):
            if x in digits:
                tmpList.append(x)
            elif x not in digits:
                numbers[counter] = int("".join(tmpList))
                tmpList = []
                counter += 1
        counter = 0
        elf1counter, elf2counter = numbers[0], numbers[2]
        while numbers[0] <= numbers[1]:
            first_elf.append(numbers[0])
            numbers[0] += 1
        while numbers[2] <= numbers[3]:
            second_elf.append(numbers[2])
            numbers[2] += 1
        if (elf2counter in first_elf) or (numbers[3] in first_elf) or (elf1counter in second_elf) or (numbers[1] in second_elf):
            final_counter += 1
        numbers = [0,0,0,0]
        first_elf = []
        second_elf = []

print ("The count for unnecessary resource distribution is :", final_counter)