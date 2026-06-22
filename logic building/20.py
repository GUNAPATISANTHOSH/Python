text = "aabbccd"
freq  = {}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in text:
    if freq[ch]==1:
        print(ch)
        break