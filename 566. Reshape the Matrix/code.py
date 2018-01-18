Collect the values of the array A, and then put them into the answer of size nR x nC.

def matrixReshape(self, A, nR, nC):
    if len(A) * len(A[0]) != nR * nC:
        return A
        
    vals = (val for row in A for val in row)
    return [[vals.next() for c in xrange(nC)] for r in xrange(nR)]
Alternative solution without generators:

def matrixReshape(self, A, nR, nC):
    if len(A) * len(A[0]) != nR * nC:
        return A
        
    vals = [val for row in A for val in row]
    ans = [[None] * nC for _ in xrange(nR)]
    i = 0
    for r in xrange(nR):
        for c in xrange(nC):
            ans[r][c] = vals[i]
            i += 1
    return ans
