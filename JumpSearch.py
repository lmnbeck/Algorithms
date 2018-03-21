import * from linearSearch

def JumpSearch(arr,blockSize,value):
    blockID = len(arr)//blockSize

    while blockID <= len(arr):
        print(blockID)
        if arr[blockID] == value:
            return blockID
        elif arr[blockID] > value:
            return linearSearch(arr,blockID-blockSize,value)
        else:
            blockID += blockSize

    return -1

#Test Function
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
result = JumpSearch(arr,4,x)
print(result)
