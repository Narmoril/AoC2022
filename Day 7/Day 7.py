total = []
counter = 0  # checks how deep in the tree the program is
dir_name = ""

# part 1

with open("Advent of Code\AoC2022\Day 7\input.txt", "r") as file:
    for line in file:
        line.strip()
        content = line.split(" ")
        if "$" in line:
            if "cd" in line:
                tmp = line.split(" ")[2]
                if ".." in tmp:
                    counter -= 1
                elif "/" in tmp:
                    pass
                else:
                    dir_name = tmp
            elif "ls" in line:
                pass
