rows = 4
# ---------- Upper Half ----------
for i in range(1, rows + 1):
    # Left stars (increasing)
    # Row1 -> 1 star
    # Row2 -> 2 stars
    for j in range(i):
        print("*", end=" ")
    # Middle spaces (decreasing)
    # Row1 -> 6 spaces
    # Row2 -> 4 spaces
    # Formula: 2 * (rows - i)
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    # Right stars (same as left)
    for j in range(i):
        print("*", end=" ")
    # Move to next row
    print()
# ---------- Lower Half ----------
for i in range(rows - 1, 0, -1):
    # Left stars (decreasing)
    # 3, 2, 1
    for j in range(i):
        print("*", end=" ")
    # Middle spaces (increasing)
    # 2, 4, 6
    for j in range(2 * (rows - i)):
        print(" ", end=" ")
    # Right stars
    for j in range(i):
        print("*", end=" ")
    print()