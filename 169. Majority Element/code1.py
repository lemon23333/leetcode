class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if count == 0:
                maj = n
            if maj == n:
                count += 1
            else:
                count -= 1
            
        return maj
