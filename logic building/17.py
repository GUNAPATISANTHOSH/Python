# Write code to count how many times each character appears in:
text = "banana"
freq={}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)