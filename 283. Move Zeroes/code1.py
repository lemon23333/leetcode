for i,n in enumerate(nums):            
            if n == 0 and i != len(nums)-1:
                j = i+1
                while nums[j] == 0 and j<len(nums)-1:
                    j += 1
                if nums[j] == 0 and j == len(nums)-1:
                    break
                else:
                    nums[i] = nums[j]
                    nums[j] = 0
