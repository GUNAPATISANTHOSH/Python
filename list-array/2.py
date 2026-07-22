s = "anagram"
t = "nagaram"
# class Solution:
#     def isAnagaram(self,s:str,t:str)->bool:
#         return sorted(s)==sorted(t)
sorted_s=sorted(s)
sorted_t=sorted(t)
if sorted_s==sorted_t:
    print(True)
else:
    print(False)