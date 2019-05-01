array = input()
array = [int(x) for x in array.split()]
n, m = array[0], array[1]

array = input()
A = [int(x) for x in array.split()]

array = input()
B = [int(x) for x in array.split()]

odd_chest = 0
for i in range(n):
    if A[i] % 2 == 1:
        odd_chest += 1

odd_keys = 0
for i in range(m):
    if B[i] % 2 == 1:
        odd_keys += 1


even_chest = n-odd_chest
even_keys = m - odd_keys

first = min(even_chest, odd_keys)
second = min(even_keys, odd_chest)

print(first + second)
