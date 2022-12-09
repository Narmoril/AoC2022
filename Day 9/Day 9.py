import numpy as np

moves = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
knots = [(0, 0), (0, 0)]
visited = set(())

# part 1, prepared for fusion with part 2

with open("input.txt", "r") as file:
    for line in file:
        nav, amount = line.split()
        amount = int(amount)

        for i in range(amount):
            kx, ky = knots[0]
            m1, m2 = moves[nav]
            knots[0] = kx + m1, ky + m2

            for k in range(1):
                kx, ky = knots[k]
                ax, ay = knots[k + 1]
                m1, m2 = kx - ax, ky - ay

                if (
                    m1**2 + m2**2 >= 4
                ):  # allows one if statement for negative and positive values of mx/my
                    knots[k + 1] = ax + np.sign(m1), ay + np.sign(m2)

            visited.add(str(knots[1]))

print("The tail of the rope visits", len(visited), "positions at least once.")

# part 2

knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
visited = set(())

with open("input.txt", "r") as file:
    for line in file:
        nav, amount = line.split()
        amount = int(amount)

        for i in range(amount):
            kx, ky = knots[0]
            m1, m2 = moves[nav]
            knots[0] = kx + m1, ky + m2

            for k in range(9):
                kx, ky = knots[k]
                ax, ay = knots[k + 1]
                m1, m2 = kx - ax, ky - ay

                if m1**2 + m2**2 >= 4:
                    knots[k + 1] = ax + np.sign(m1), ay + np.sign(m2)

            visited.add(str(knots[9]))

print("After the rope snaps, the tail of the rope visits", len(visited), "positions at least once.")
