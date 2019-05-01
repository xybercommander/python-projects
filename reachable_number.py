#url to the problem --> http://codeforces.com/contest/1157/problem/A
import random
num = int(input())
num_list = set()
#adding the first number to the set
num_list.add(num)

while num > 1:
    num += 1
    while(num % 10 == 0):
        num /= 10
    num_list.add(num)
    for i in range(2,10):
        num_list.add(i)

print(len(num_list))
