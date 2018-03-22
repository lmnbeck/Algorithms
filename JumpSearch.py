import * from linearSearch
import math

def JumpSearch(arr,value):
    step = int(math.sqrt(len(arr)))
    blockID = step
    while blockID <= len(arr):
        print(blockID)
        if arr[blockID] == value:
            return blockID
        elif arr[blockID] > value:
            return linearSearch(arr,blockID-step,value)
        else:
            blockID += step

    return -1

#Test Function
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
result = JumpSearch(arr,x)
print("result = ",result)
