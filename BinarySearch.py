
def BinarySearch(arr,l,r,value):
    while l <= r:
        i = l + (r-l)//2
        print(i)
        if arr[i] == value:
            return i
        elif arr[i] < value:
            l = i + 1
        else:
            r = i - 1
    return -1

#Test Function
arr = [1 ,2 ,4, 5, 6,65, 454,1233]
x = 43
result = BinarySearch(arr,0,len(arr)-1,x)
print(result)
