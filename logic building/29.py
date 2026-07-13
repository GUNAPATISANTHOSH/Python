s = "Python 123"
letters = 0
digits = 0
spaces = 0
for ch in s:
    if ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters += 1
    elif ch in "0123456789":
        digits += 1
    elif ch == " ":
        spaces += 1
print("Letters =", letters)
print("Digits =", digits)
print("Spaces =", spaces)