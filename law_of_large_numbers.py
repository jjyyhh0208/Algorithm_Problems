n, m, k = list(map(int, input().split()))

input_list = list(map(int, input().split()))
input_list.sort(reverse=True)

biggest = input_list[0]
second_biggest = input_list[1]


def calculate_answer(m, k, biggest, second_biggest):
    cluster = (biggest * k + second_biggest)
    cluster_num = (m // (k+1))
    remaining = biggest * (m % (k+1))
    
    result = cluster * cluster_num + remaining
    return result

print(calculate_answer(m, k, biggest, second_biggest))