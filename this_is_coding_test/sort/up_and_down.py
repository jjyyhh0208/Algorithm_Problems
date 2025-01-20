n = int(input())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)
    
nums.sort()
nums.reverse()

print(nums)
