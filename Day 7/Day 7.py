path = []
dir_list = []
dir_size = {}
tmp = 0  # tmp is being used here to the total amount used for the answer

# part 1

with open("Day 7\input.txt", "r") as file:
    for line in file:
        line.strip()
        content = line.strip().split(" ")
        if content[0] == "$":
            if content[1] == "cd":
                if content[2] == "..":
                    dir_list.pop()
                elif content[2] == "/":
                    dir_list = ["/"]
                else:
                    dir_list.append(content[2])
        elif content[0].isnumeric():
            path = ["".join(dir_list[: x + 1]) for x in range(len(dir_list))]
            for x in path:
                if x not in dir_size:
                    dir_size[x] = 0
                dir_size[x] += int(content[0])
    for x in dir_size:
        if dir_size[x] <= 100000:
            tmp += dir_size[x]

print("The total size of the requested directories is:", tmp)

# part 2

tmp = 0  # tmp is being used to store the size of the (so far) smallest directory that works as an answer
free_space = 70000000 - dir_size["/"]
required_space = 30000000 - free_space

for x in dir_size:
    if dir_size[x] > required_space:
        if tmp == 0:
            tmp = dir_size[x]
        elif dir_size[x] < tmp:
            tmp = dir_size[x]

print("The smallest directory to free up enough space is:", tmp)
