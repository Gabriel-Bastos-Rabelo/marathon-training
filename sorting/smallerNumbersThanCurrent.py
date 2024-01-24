def smallerNumbersThanCurrent(nums):
    
    enumerated_nums = list(enumerate(nums))

    enumerated_nums.sort(key=lambda x: x[1])

    smaller_count = {}
    for i, (original_index, value) in enumerate(enumerated_nums):
        
        if value not in smaller_count:
            smaller_count[value] = i

    result = [smaller_count[num] for num in nums]

    return result

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
