#Problem: Find the Most Frequent Character
text = "mississippi"
freq={}

for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch] = 1
max_count=0
for ch in freq:
    if freq[ch]>max_count:
        max_count=freq[ch]
for ch in freq:
    if freq[ch] == max_count:
        print(ch,freq[ch])