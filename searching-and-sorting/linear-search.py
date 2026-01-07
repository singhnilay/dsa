def linearSearch(arr, key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index
        
    return -1
        

lst = [2,1,3,4,5,2,2,1]

print(linearSearch(lst,5))