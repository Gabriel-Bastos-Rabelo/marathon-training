
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        initPoint = 0
        endPoint = len(nums) - 1
        while initPoint <= endPoint:
            if initPoint == i:
                initPoint += 1
            if endPoint == i:
                endPoint -= 1
            if initPoint >= endPoint:
                break
            soma = nums[initPoint] + nums[endPoint]

            if soma > (nums[i] * -1):
                endPoint -= 1
            elif soma < (nums[i] * -1):
                initPoint += 1
            else:
                triplet = sorted([nums[i], nums[initPoint], nums[endPoint]])
                if triplet not in res:
                    res.append(triplet)
                initPoint += 1
                endPoint -= 1

    return res

print(threeSum([-1,0,1,0]))
    
