def primes(num):
    count = 0
    list1 = [2]
    a = 3
    if num < 2:
        return 0
    else:
        while a < num:
            for i in range(3,a):
                if a % i == 0:
                    a += 2
                    break
            else:
                count += 1
                a+=2
    return count + 1

print(primes(10))
