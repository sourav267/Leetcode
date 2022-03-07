class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            setCheck1 = set()
            setCheck2 = set()
            for j in range(n):
                if matrix[i][j] in setCheck1 or matrix[j][i] in setCheck2:return False
                else:
                    setCheck1.add(matrix[i][j])
                    setCheck2.add(matrix[j][i])
                
                    
        return True
                
        