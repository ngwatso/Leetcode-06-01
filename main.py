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

from collections import deque

class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.index = 0
        

    def insert(self, key: int, value: str) -> List[str]:
        self.arr[key-1] = value
        newArr = []
        
        if (key - 1) == self.index:
            for i in range(self.index, len(self.arr)):
                if self.arr[self.index] == None:
                    break
                else:
                    newArr.append(self.arr[self.index])
                    self.index += 1
            
            return newArr


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

# ===============

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        word_1 = "".join(word1)
        word_2 = "".join(word2)
        
        if word_1 == word_2:
            return True
        else:
            return False
        
        # Method 2
        # return "".join(word1) == "".join(word2)

# ===============