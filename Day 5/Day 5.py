cargo = [[],[],[],[],[],[],[],[],[]]
stack_counter = 0
counter = 0
move_args = ["0","0","0"]

# part 1

with open("input.txt", "r") as file:
    for line in file:
        if "[" in line:
            for x in line:
                counter += 1
                if x.isalpha():
                    cargo[stack_counter].append(x)
                if counter == 2 or counter == 6 or counter == 10 or counter == 14 or counter == 18 or counter == 22 or counter == 26 or counter == 30:
                    stack_counter += 1
                if counter > 34:
                    stack_counter = 0
            counter = 0
        elif line.strip() == "": # after having some issues, I found out that the original order of the crates is reversed in my code
            tmp = 8
            while tmp >= 0:
                cargo[tmp].reverse()
                tmp -= 1
        elif "move" in line:
            for x in line:
                if x.isnumeric():
                    move_args[counter] = x
                    if tmp.isnumeric():
                        move_args[0] = "".join(move_args[:2])
                        counter = 0
                    counter += 1
                tmp = x
            counter = 0
            while int(move_args[0]) > 0:
                tmp = cargo[int(move_args[1]) - 1][-1]
                del(cargo[int(move_args[1]) - 1][-1])
                cargo[int(move_args[2]) - 1].append(tmp)
                move_args[0] = int(move_args[0]) - 1

print("The top crates are: ", cargo[0][-1], cargo[1][-1], cargo[2][-1], cargo[3][-1], cargo[4][-1], cargo[5][-1], cargo[6][-1], cargo[7][-1], cargo[8][-1], sep = "")

# part 2
# made an error here where I forgot to reset the variables (so part 2 worked independently, but not when I also ran part 1)
cargo = [[],[],[],[],[],[],[],[],[]]
stack_counter = 0
counter = 0
move_args = ["0","0","0"]

with open("input.txt", "r") as file:
    for line in file:
        if "[" in line:
            for x in line:
                counter += 1
                if x.isalpha():
                    cargo[stack_counter].append(x)
                if counter == 2 or counter == 6 or counter == 10 or counter == 14 or counter == 18 or counter == 22 or counter == 26 or counter == 30:
                    stack_counter += 1
                if counter > 34:
                    stack_counter = 0
            counter = 0
        elif line.strip() == "":
            tmp = 8
            while tmp >= 0:
                cargo[tmp].reverse()
                tmp -= 1
        elif "move" in line:
            for x in line:
                if x.isnumeric():
                    move_args[counter] = x
                    if tmp.isnumeric():
                        move_args[0] = "".join(move_args[:2])
                        counter = 0
                    counter += 1
                tmp = x
            counter = 0
            while int(move_args[0]) > 0:
                tmp = cargo[int(move_args[1]) - 1][- int(move_args[0])]
                del(cargo[int(move_args[1]) - 1][- int(move_args[0])])
                cargo[int(move_args[2]) - 1].append(tmp)
                move_args[0] = int(move_args[0]) - 1

print("The corrected top crates are: ", cargo[0][-1], cargo[1][-1], cargo[2][-1], cargo[3][-1], cargo[4][-1], cargo[5][-1], cargo[6][-1], cargo[7][-1], cargo[8][-1], sep = "")