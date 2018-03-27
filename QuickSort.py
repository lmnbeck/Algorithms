# The key process in quickSort is partition(). 
# Target of partitions is, given an array and an element x of array as pivot, 
# put x at its correct position in sorted array and put all smaller elements
# (smaller than x) before x, and put all greater elements (greater than x) after x. 
# All this should be done in linear time.

def partitions(arr,low,high):
    
    if low <= high:
        i = low -1
        for j in range(low,high):
            if arr[j] <= arr[high]:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]
            j += 1
    i += 1
    arr[i],arr[high] = arr[high],arr[i]
    
    return i
    
def quickSort(arr,low,high):
    if low < high:
        pi = partitions(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    
    
# Driver code to test above
arr = [10, 7, 4,3,8,2, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d " %arr[i],end = "")
 
