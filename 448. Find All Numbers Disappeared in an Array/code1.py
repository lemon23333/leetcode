a = [0]
if len(nums) != 0:
    for i in range(1,len(nums)+1):
        if nums.count(i) == 0:
            a.append(i)

return a
