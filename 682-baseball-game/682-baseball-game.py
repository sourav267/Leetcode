class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr=[]
        for i,e in enumerate(ops):
            if e == 'C':
                arr.pop()
            elif e == 'D':
                arr.append(arr[-1]*2)
            elif e == '+':
                arr.append(arr[-1] + arr[-2])
            else:
                arr.append(int(e))
            
        return sum(arr)
                
        