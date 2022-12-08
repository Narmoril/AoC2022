forest = []
trees = []
row = 0
column = 0
visible_trees = set()
counter = 0

# creating a matrix of the forest
with open("Advent of Code\AoC2022\Day 8\input.txt", "r") as file:
    for line in file:
        for x in line.strip():
            trees.append(x)
        forest.append(trees)
        trees = []


def visible_left(visible_trees, forest, row, column):
    while row <= 98:
        for x in forest[row]:
            if column == 0:
                visible_trees.add((row, column))
            else:
                if int(forest[row][column]) > int(forest[row][column - 1]):
                    visible_trees.add((row, column))
                elif int(forest[row][column]) <= int(forest[row][column - 1]):
                    visible_trees.add((row, column))
            column += 1
    return visible_trees()


print(visible_left(visible_trees, forest, row, column))

"""

while row <= 98:
    for x in forest[row]:
        if column == 0:
            visible_trees.add((row, column))
        else:
            if int(forest[row][column]) > int(forest[row][column - 1]) and counter == 0:
                visible_trees.add((row, column))
            elif (
                int(forest[row][column]) <= int(forest[row][column - 1])
                and counter == 0
            ):
                visible_trees.add((row, column))
                counter = 1
        if int(forest[row][column]) < int(forest[row][column - 1]) and counter == 1:
            tmp += 1
        elif int(forest[row][column]) == int(forest[row][column - 1]) and counter == 1:
            tmp = 1
        elif int(forest[row][column]) > int(forest[row][column - 1]) and counter == 1:
            tmp = 0
        if column == 98:
            visible_trees.add((row, column))
        column += 1

    counter = 0
    column = 0
    row += 1

print(len(visible_trees))

"""

"""

    if row == 0 or row == 98:
        visible_trees += len(forest[row])
    elif 0 < row < 98:
        while column <= 98:
            if int(forest[row][column]) > int(forest[row][column - 1]) and counter == 0:
                pass
            elif (
                int(forest[row][column]) <= int(forest[row][column - 1])
                and counter == 0
            ):
                top_left = forest[row][column]
                counter = 1
            elif (
                int(forest[row][column]) < int(forest[row][column - 1]) and counter == 1
            ):
                tmp += 1
            elif (
                int(forest[row][column]) == int(forest[row][column - 1])
                and counter == 1
            ):
                tmp = 1
            elif (
                int(forest[row][column]) > int(forest[row][column - 1]) and counter == 1
            ):
                tmp = 0
            if column == 98:
                visible_trees += tmp + 1
            column += 1
        counter = 0
        column = 0
    row += 1


print(visible_trees)
print(len(forest[0]) * 99)
"""
