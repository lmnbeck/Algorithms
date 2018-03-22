def InterpolationSearch(arr,x):
    Hi = len(arr)-1
    Li = 0
    pos = Li + int((Hi-Li)/(arr[Hi]-arr[Li])*(x-arr[Li]))
    while pos <= Hi:
        print(pos)
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            Li = pos + 1
        else:
            Hi = pos - 1
        pos = Li + int((Hi-Li)/(arr[Hi]-arr[Li])*(x-arr[Li]))
    return -1

# Driver Code
# Array of items oin which search will be conducted
arr = [10, 12, 13, 16, 18, 19, 20, 21, \
				22, 23, 24, 33, 35, 42, 47]
n = len(arr)

x = 42 # Element to be searched
index = InterpolationSearch(arr, x)

if index != -1:
	print("Element found at index",index)
else:
	print("Element not found")
