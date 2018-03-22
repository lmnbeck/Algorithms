'''
The idea is to start with subarray size 1 compare its last element with x, 
then try size 2, then 4 and so on until last element of a subarray is not greater.
Once we find an index i (after repeated doubling of i), we know that the element 
must be present between i/2 and i (Why i/2? because we could not find a greater value
in previous iteration)
'''
def binarySearch( arr, l, r, x):
    if r >= l:
        mid = int(l + ( r-l ) / 2)
         
        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If the element is smaller than mid, then it
        # can only be present in the left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
         
        # Else he element can only be present in the right
        return binarySearch(arr, mid+1, r, x)
         
    # We reach here if the element is not present
    return -1
def exponentialSearch(arr, x):
    i = 1
    if arr[0] == x:
        return 1
    
    while i <= len(arr)-1:
        print(i)
        if arr[i] == x:
            return i
        elif arr[i] < x:
            i = i * 2
        else:
            return binarySearch(arr,i//2,i,x)
    return -1
    
# Driver Program
 
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponentialSearch(arr, x)
if result == -1:
    print ("Element not found in thye array")
else:
    print ("Element is present at index %d" %(result))
