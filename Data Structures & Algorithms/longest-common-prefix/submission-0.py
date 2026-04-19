class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs[0])
        prefix=""
        for i in range(n):
            temp = strs[0][i]
            for ele in strs:
                if i>=len(ele) or ele[i]!=temp:
                    return prefix
                    exit()
            prefix += temp
        return prefix 
    
        