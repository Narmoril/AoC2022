def day_6(tmp, marker):
    with open("Advent of Code\\AoC2022\Day 6\input.txt", "r") as file:
        counter = 0
        for line in file:
            for x in line:
                marker = marker[1:] + [x]
                counter += 1
                if counter > tmp and len(marker) == len(set(marker)):
                    return counter
                    break


print("The start-of-packet marker appears after character:", day_6(3, ["", "", "", ""]))
print(
    "The start-of-message marker appears after character:",
    day_6(13, ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]),
)
