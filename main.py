class Solution:
    def maxDepth(self, s: str) -> int:
        
        count = 0
        maxDepth = 0
        
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                if count > maxDepth:
                    maxDepth = count
                count -= 1
            else:
                continue
                
        return maxDepth

# ===============

