#Bubble Sort is the simplest sorting algorithm 
#that works by repeatedly swapping the adjacent elements if they are in wrong order.

def bubbleSort(arr):
    for j in range(len(arr)):
        for i in range(0,len(arr)-j-1):
            if arr[i] >= arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 1 
        j += 1 
    
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90,2,3,1]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 
