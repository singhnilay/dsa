def binarySearch(arr, key):
    n = len(arr)
    start = 0
    end = n-1
    middle = ( start + end ) // 2
     
    while (start <= end) :
        middle = (start + end) // 2

        if arr[middle] > key :
            end = middle - 1

        elif arr[middle] < key : 
            start = middle + 1

        elif arr[middle] == key :
            return middle
    

    return -1 


lst = [1,2,3,4,5,6,7,8]

print(binarySearch(lst, 3))