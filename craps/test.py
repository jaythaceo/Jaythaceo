

def binarySearch(array, x, low , high):
    """Repeat until the pointers low and high meet each other"""
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid -1
    return -1

array = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
x = 7

result  = binarySearch(array, x, 0, len(array)-1) 

if result != -1:
    print(array)
    print("Element is present at index " + str(result))
else:
    print("Not Found")

