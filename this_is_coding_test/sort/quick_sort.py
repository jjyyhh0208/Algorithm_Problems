array = [2, 1, 5, 3, 4, 7, 8, 6, 9, 0]

def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))