class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            setCheck = set()
            for j in range(n):
                if matrix[i][j] in setCheck:return False
                else:setCheck.add(matrix[i][j])
        
        for i in range(n):
            setCheck = set()
            for j in range(n):
                if matrix[j][i] in setCheck:return False
                else:setCheck.add(matrix[j][i])
                    
        return True
                
        