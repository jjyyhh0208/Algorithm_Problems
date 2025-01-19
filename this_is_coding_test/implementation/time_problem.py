hour = 0
n = int(input())
count = 0

while hour < n + 1:
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1
        minute += 1
    hour += 1
    
print(count)