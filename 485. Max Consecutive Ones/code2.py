class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcou=0
        count=0
        for num in nums:
            if num == 0:
                maxcou=max(count,maxcou)
                count=0
            else:
                count+=1
        maxcou=max(count,maxcou)
        return maxcou
