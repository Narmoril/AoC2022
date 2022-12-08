forest = []
trees = []
visible = 0
scenic_score_ = 0

# creating a matrix of the forest
with open("Advent of Code\AoC2022\Day 8\input.txt", "r") as file:
    for line in file:
        for x in line.strip():
            trees.append(x)
        forest.append(trees)
        trees = []


def scenic_score(var, val, arr):
    first_half = list(reversed(arr[:var]))
    second_half = arr[var + 1 :]
    view1 = len(first_half)
    for i in range(len(first_half)):
        if first_half[i] >= val:
            view1 = i + 1
            break
    view2 = len(second_half)
    for i in range(len(second_half)):
        if second_half[i] >= val:
            view2 = i + 1
            break
    view = view1 * view2
    return view


visible = (len(forest) + len(trees[1:-1])) * 2

for row in range(1, len(forest) - 1):
    for col in range(1, len(forest[0]) - 1):
        val = forest[row][col]
        if (
            max([x[col] for x in forest][:row]) < val
            or max(x[col] for x in forest[row + 1 :]) < val
            or max(forest[row][:col]) < val
            or max(forest[row][col + 1 :]) < val
        ):
            visible += 1
        row_ = scenic_score(col, val, forest[row])
        column = scenic_score(row, val, [x[col] for x in forest])
        scenic_score_ = max(scenic_score_, row_ * column)


print(visible, "trees are visible from outside the grid.")
print("The highest scenic score is:", scenic_score_)
