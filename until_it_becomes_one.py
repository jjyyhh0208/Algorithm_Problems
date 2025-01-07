def select_option(n, k):
    if n % k == 0:
        return '2'
    else:
        return '1'
    
def generate_option(count, opt, n, k):
    if opt == '1':
        n -= 1
    elif opt == '2':
        n = int(n / k)
    count += 1
    
    return n, count
        
n, k = list(map(int, input().split()))
opt = None
count = 0

while True:
    if n == 1:
        break
    opt = select_option(n, k)
    n, count = generate_option(count, opt, n, k)
    
print(count)