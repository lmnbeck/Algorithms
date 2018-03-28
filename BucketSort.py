'''
bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
.......a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
'''
import numpy as np

def bucketSort(arr):
    n = len(arr)
    j = 0

    arr2 = [0.0 for i in range(n*1000)]
    #for i in range(len(arr2)):
        #print ("%f " %arr2[i],end = "")
    for i in range(n):
        print("i=",i)
        arr2[int(arr[i]*1000)] = arr[i]
        print("arr[i]=",arr[i])
    for i in range(len(arr2)):
        if arr2[i] != 0.0:
            arr[j] = arr2[i]
            j += 1

# Driver code to test above
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
n = len(arr)
#arr.sort()
bucketSort(arr)
print ("Sorted array is:")
for i in range(n):
    print ("%f " %arr[i],end = "")
