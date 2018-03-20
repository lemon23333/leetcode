a = [0]*len(nums)
for n in nums:
    a[n-1] += 1

return [i+1 for i in range(len(nums)) if a[i] == 0]
