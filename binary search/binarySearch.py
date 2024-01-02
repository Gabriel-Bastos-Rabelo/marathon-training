lista = [9,6,4,2,3,5,7,0,1]
lista.sort()



def binarySearch(target, nums):
    l = 0
    r = len(nums)
    while(l < r):
        mid = l + (r - l)//2
        if(nums[mid] <= target):
            l = mid

        else:
            r = mid - 1

    print(l)




binarySearch(3, lista)