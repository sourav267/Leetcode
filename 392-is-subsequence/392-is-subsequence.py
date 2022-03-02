class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        c = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i=i+1
                j=j+1
                c=c+1
            else:
                j=j+1
        if c == len(s):
            return True
        else:
            return False
        