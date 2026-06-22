text="mississippi"
freq={}
for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
max=0
for ch in freq:
    if freq[ch]>max:
        max=freq[ch]
for ch in freq:
    if freq[ch]==max:
        print(ch,freq[ch])