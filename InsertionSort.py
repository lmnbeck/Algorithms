#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
'''
Insertion Sort

Algorithm
// Sort an arr[] of size n
insertionSort(arr, n)
Loop from i = 1 to n-1.
……a) Pick element arr[i] and insert it into sorted sequence arr[0…i-1]
'''
def insertionSort(arr):
    for j in range(1,len(arr)):
        i=j
        while i > 0:
            if arr[i] < arr[i-1]:
                arr[i] , arr[i-1] = arr[i-1] , arr[i]
            i = i - 1
        j += 1

# Driver code to test above
arr = [12, 11, 13, 5, 6,34,55,6,6423,4,6,34,435,345]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
