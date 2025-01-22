import sys

def binary_search(arr: list, target: int, start: int, end: int):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

def find_parts(total_parts: list, request_parts: list):
    result_str = ""
    for part in request_parts:
        if binary_search(total_parts, part, 0, len(total_parts)-1) == None:
            result_str += 'no '
        else:
            result_str += 'yes '
    return result_str
        

n = int(input())
total_parts = list(map(int, sys.stdin.readline().rstrip().split()))
total_parts.sort()

m = int(input())
request_parts = list(map(int, sys.stdin.readline().rstrip().split()))

result = ""

result += find_parts(total_parts, request_parts)

print(result)