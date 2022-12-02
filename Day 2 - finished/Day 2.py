
# part 1
# A, X for rock
# B, Y for paper
# C, Z for scissors

total_score = 0

with open("input.txt", "r") as file:
    for line in file:
        if "X" in line.strip():
            if "A" in line.strip():
                total_score += 3
            elif "C" in line.strip():
                total_score += 6
            total_score += 1

        elif "Y" in line.strip():
            if "B" in line.strip():
                total_score += 3
            elif "A" in line.strip():
                total_score += 6
            total_score += 2

        elif "Z" in line.strip():
            if "C" in line.strip():
                total_score += 3
            elif "B" in line.strip():
                total_score += 6
            total_score += 3

print("The total score would be ", total_score, ".", sep="")


# part 2
# A for rock
# B for paper
# C for scissors
# X for needing to lose
# Y for needing to draw
# Z for needing to win

total_score_correct = 0

with open("input.txt", "r") as file:
    for line in file:
        if "X" in line.strip(): # need to lose
            if "A" in line.strip(): # scissors
                total_score_correct += 3
            elif "B" in line.strip(): # rock
                total_score_correct += 1
            elif "C" in line.strip(): # paper
                total_score_correct += 2

        elif "Y" in line.strip(): # need to draw
            if "A" in line.strip(): # rock
                total_score_correct += 1
            elif "B" in line.strip(): # paper
                total_score_correct += 2
            elif "C" in line.strip(): # scissors
                total_score_correct += 3
            total_score_correct += 3

        elif "Z" in line.strip(): # need to win
            if "A" in line.strip(): # paper
                total_score_correct += 2
            elif "B" in line.strip(): # scissors
                total_score_correct += 3
            elif "C" in line.strip(): # rock
                total_score_correct += 1
            total_score_correct += 6

print("The corrected total score would be ", total_score_correct, ".", sep="")