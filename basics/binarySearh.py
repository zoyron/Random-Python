def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

arr = [1,2,3,4,5,6,7,8,9,10]

ans = binarySearch(arr, 7)
if ans == -1:
    print("The target is not present in the array")
else:
    print(f"The target is present at index {ans} in the array")
