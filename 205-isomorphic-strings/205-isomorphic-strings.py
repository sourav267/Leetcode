class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        hmap = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = t[i]
                if t[i] in used:
                    return False
                used.add(t[i])
            if hmap[s[i]] != t[i]:
                return False
        return True
        
        