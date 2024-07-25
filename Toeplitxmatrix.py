class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        
        rows, cols = len(matrix), len(matrix[0])
        diagonals = {}
        
        for i in range(rows):
            for j in range(cols):
                diagonal = i - j
                if diagonal not in diagonals:
                    diagonals[diagonal] = matrix[i][j]
                elif matrix[i][j] != diagonals[diagonal]:
                    return False
        
        return True

        
