array = [2, 1, 5, 3, 4, 7, 8, 6, 9, 0]

def select_sort(arr: list):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
select_sort(array)
print(array)