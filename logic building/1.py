#Find how many vowels (a, e, i, o, u) are present in the string.
text = "programming"
count=0
vowels= "aeiou"
for ch in text:
    if ch in vowels:
        # count +=1
        print(ch)

