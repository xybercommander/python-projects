def blackjack(a,b,c):
    sum = a+b+c
    if sum <= 21:
        return sum
    elif sum > 21 and 11 in (a,b,c):
        new_sum = sum-10
        if new_sum <= 21:
            return new_sum
        else:
            return 'BUST'
    elif sum > 21 and 11 not in (a,b,c):
        return 'BUST'

print(blackjack(9,9,9))
