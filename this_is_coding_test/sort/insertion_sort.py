array = [2, 1, 5, 3, 4, 7, 8, 6, 9, 0]


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

insertion_sort(array)
print(array)