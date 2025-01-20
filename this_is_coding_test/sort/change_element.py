n, k = list(map(int, input().split()))
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))
    
lista.sort()
listb.sort(reverse=True)

for i in range(k):
    if lista[i] < listb[i]:
        lista[i], listb[i] = listb[i], lista[i]
    else:
        continue
print(sum(lista))