class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        j = n - 1
        i = 0
        l = []
        while i<j:
            
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] == target:
                l.append(i+1)
                l.append(j+1)
                return l

    
        
