nums = [1,2,3,4,5]


while True:
    if len(nums) == 1:
        print(nums[0])
    newNums = [0] * (len(nums)-1)
    for i in range(0, len(nums)-1):
        newNums[i] = (nums[i] + nums[i+1]) % 10

    

    nums = newNums