# Write code to count the vowels in:
text = "programming"
count=0
vowels="aeiou"
for ch in text:
    if ch in vowels:
        count+=1
print(count)