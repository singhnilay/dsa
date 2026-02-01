# this solution implements two sum 2 using two pointer algorithm.

def twoSum(arr, target):
    n = len(arr)
    l = 0
    r = n-1

    while l < r:
        if arr[l] + arr[r] == target:
         return [l+1, r+1]

        elif arr[l] + arr[r] < target:
            l += 1

        else: 
            r -= 1

lst = [10,13,19,21]

target = 29

print(twoSum(lst, target))

    