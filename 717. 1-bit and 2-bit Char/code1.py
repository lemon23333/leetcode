class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        if bits[-2] == 0:
            return True
        f = 0
        for i in range(2,len(bits)+1):
            if bits[i*(-1)] == 1:
                f += 1
            else:
                if f % 2 == 1:
                    return False
                else:
                    return True
        if f % 2 == 1:
            return False
        return True
        
