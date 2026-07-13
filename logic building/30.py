s = "Python is Fun 123"
vowels = 0
consonants = 0
digits = 0
spaces = 0
for ch in s:
    if ch in "aeiouAEIOU":
        vowels+=1
    elif ch in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants+=1
    elif ch in "0123456789":
        digits+=1
    elif ch in " ":
        spaces+=1
print("vowels = ",vowels) 
print("consonants = ",consonants) 
print("digits = ",digits) 
print("spaces = ",spaces) 