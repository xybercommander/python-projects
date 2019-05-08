def lol(mylist): #[1,2,3,6,7,8,9,1,2] --> 9
    total = 0
    e = True
    for i in mylist:
        if e == True:
            if i != 6:
                total += i
            else:
                e = False
        elif e == False:
            if i == 9:
                e = True
    return total


print(lol([1,2,3,6,7,8,9,1,2]))
