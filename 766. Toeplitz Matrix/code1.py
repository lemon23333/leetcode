#第一列和第一行与斜线上数据相等
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])
        for j in range(c):
            for i in range(r):
                if (j+i)<c and matrix[0][j] != matrix[i][j+i]:
                    return False
        for i in range(r):
            for j in range(c):
                if (i+j)<r and matrix[i][0] != matrix[i+j][j]:
                    return False
        return True
