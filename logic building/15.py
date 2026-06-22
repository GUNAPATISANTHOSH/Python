# Write code to count consonants in:
text = "programming"
count=0
vowels="aeiou"
for ch in text:
    if ch not in vowels:
        count+=1
print(count)