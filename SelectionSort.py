#code
import sys
A = [64, 25, 12, 22, 11]

def selectionSort(arr,start):
    i= start
    result = start
    if start >= len(arr)-1:
        return -1
    else:
        while i <= (len(arr)-1):
            if arr[result] >= arr[i]:
                arr[result],arr[i]=arr[i],arr[result]
            i = i + 1
    selectionSort(arr,start+1)
    
# Driver code to test above
print ("Sorted array")
selectionSort(A,0)
for i in range(len(A)):
    print("%d" %A[i]), 
