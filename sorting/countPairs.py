#solução 1

def countPairs(self, nums: List[int], target: int) -> int:
    tamanho = len(nums)
    res = 0
    nums.sort()
    final = tamanho
    for i in range(tamanho):
        for j in range(i + 1, final):
            if nums[i] + nums[j] < target:
                res += 1
            else:
                final -= 1
                break

    return res

#solução 2
def countPairs(self, nums: List[int], target: int) -> int:

    def mergeSort(array):
        size = len(array)
        mid = size//2

        if(size == 1):
            return array
        elif(size == 0):
            return []
        elif(size == 2):
            if(array[0] > array[1]):
                array[0], array[1] = array[1], array[0]
            return array

        else:
            l = array[:mid]
            r = array[mid:]
            mergeSort(l)
            mergeSort(r)

            left = 0
            right = 0
            index = 0
            while(left < len(l) and right < len(r)):
                if l[left] < r[right]:
                    array[index] = l[left]
                    left += 1
                else:
                    array[index] = r[right]
                    right += 1

                index += 1

            while(left < len(l)):
                array[index] = l[left]
                left += 1
                index += 1

            while(right < len(r)):
                array[index] = r[right]
                right += 1
                index += 1

            return array

    tamanho = len(nums)
    res = 0
    left = 0
    right = tamanho-1
    nums = mergeSort(nums)
    print(nums)
    while(left < right):
        at = nums[left] + nums[right]
        if(at < target):
            res += (right - left)
            left += 1
        elif(at >= target):
            right -= 1

    return res
           