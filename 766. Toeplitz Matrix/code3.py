class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
                   
   

For each diagonal with elements in order a1,a2,a3,…,ak
, we can check a1=a2,a2=a3,…,ak−1=ak
. The matrix is Toeplitz if and only if all of these conditions are true for all (top-left to bottom-right) diagonals.

Every element belongs to some diagonal, and it's previous element (if it exists) is it's top-left neighbor. Thus, for the square (r, c), we only need to check r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c].


Complexity Analysis

Time Complexity: O(M∗N), as defined in the problem statement.

Space Complexity: O(1).
