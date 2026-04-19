class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for st in s:
            if st in d:
                d[st]+=1
            else:
                d[st]=1
        for st in t:
            if st in d:
                d[st]-=1
            else:
                return False    
        for k,v in d.items():
            if v==0:
                continue
            else:
                return False
                break
        return True 


        