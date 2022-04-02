class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = dict()
        for i in s:
            try:
                map[i] += 1
            except:
                map[i] = 1
        
        for i,c in enumerate(s):
            if map[c] == 1:
                return i
        return -1
                
        