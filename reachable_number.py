num = int(input())
num_list = set()

num_list.add(num)

while n != 0:
    num += 1
    while(num % 10 == 0):
        num /= 10
    num_list.add(num)
    for i in range(2,10):
        num_list.add(i)

print(len(num_list))
