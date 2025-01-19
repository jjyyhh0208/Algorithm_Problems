n, m = list(map(int, input().split()))
row_list = []
minimum_in_each_row = []

def build_matrix(n):
    for _ in range(n):
        row = list(map(int, input().split()))
        row_list.append(row)
    
def find_minimum_in_each_row(row_list):
    for list in row_list:
        minimum = min(list)
        minimum_in_each_row.append(minimum)
        
def find_answer(minimum_in_each_row):
    result = max(minimum_in_each_row)
    return result

build_matrix(n)
find_minimum_in_each_row(row_list)
answer = find_answer(minimum_in_each_row)

print(answer)