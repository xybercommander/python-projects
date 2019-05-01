#url to the problem --
#http://codeforces.com/contest/1152/problem/A

#for inputting the n and m values which stand for the number of chests
#and the number of keys
array = input()
#we are taking a whole string as input but in the next line we are splitting
#the numbers in the string into a list to take it in as an array
arr = [int(x) for x in array.split()]
n = arr[0]
m = arr[1]

#inputting the number of chests
array = input()
#we are taking a whole string as input but in the next line we are splitting
#the numbers in the string into a list to take it in as an array
chests = [int(x) for x in array.split()]

#inputting the number of keys
array = input()
#we are taking a whole string as input but in the next line we are splitting
#the numbers in the string into a list to take it in as an array
keys = [int(x) for x in array.split()]

e_keys = 0
o_keys = 0
e_chests = 0
o_chests = 0

#counting the number of even and odd chests
for i in range(n):
    if chests[i] % 2 != 0:
        o_chests += 1
    else:
        e_chests += 1

#counting the number of even and odd keys
for i in range(m):
    if keys[i] % 2 != 0:
        o_keys += 1
    else:
        e_keys += 1


o_k_e_c = min(o_keys, e_chests) #o_k_e_c = odd keys and even chests
o_c_e_k = min(e_keys, o_chests) #o_c_e_k = even keys and odd chests
#We can get the result like this because odd + even is always odd

print(o_c_e_k + o_k_e_c)
