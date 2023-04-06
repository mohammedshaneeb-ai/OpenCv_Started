nums = [2,7,11,15]
target = 9
output = []
for i in range(len(nums)):
    for j in range(len(nums)+1):
        if nums[i] + nums[j] == target:
            print(i, j)
        else:
            continue
print(output)

