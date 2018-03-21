def linearSearch(array, fromIDx, value ):
    for i in range(fromIDx,len(array)):
        if array[i] == value:
            return i
    return -1

#Test Function
arr = [1 ,2 ,4, 5, 6,65, 454,1233]
x = 10
result = linearSearch(arr,0,x)
print(result)
