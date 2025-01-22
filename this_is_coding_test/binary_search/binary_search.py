def binary_search(arr: list, target: int, left: int, right: int):
    if left > right:
        return None

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

array = [0, 2, 4, 6, 8, 10, 12, 14, 16]
target = 16

print(binary_search(array, target, 0, len(array) - 1))
