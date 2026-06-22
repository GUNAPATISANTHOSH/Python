# We want the first non-repeating character.
text = "swiss"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
# print(freq)
for ch in text:
    if freq[ch]==1:
        print(ch)
        break