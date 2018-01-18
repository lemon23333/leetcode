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
                if count>maxcou:
                    maxcou=count
                count=0
            else:
                count+=1
        if count>maxcou:
            maxcou=count 
        return maxcou
