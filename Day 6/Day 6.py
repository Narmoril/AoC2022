marker = ["", "", "", ""]
counter = 0

# part 1

with open("Advent of Code\\2022\Day 6\input.txt", "r") as file:
    for line in file:
        for x in line:
            marker = marker[1:] + [x]
            counter += 1
            if counter > 3 and len(marker) == len(set(marker)):
                break

print("The start-of-packet marker appears after  the", counter, "th character")

# part 2

marker = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
counter = 0

with open("Advent of Code\\2022\Day 6\input.txt", "r") as file:
    for line in file:
        for x in line:
            marker = marker[1:] + [x]
            counter += 1
            if counter > 13 and len(marker) == len(set(marker)):
                break

print("The start-of-message marker appears after  the", counter, "th character")
