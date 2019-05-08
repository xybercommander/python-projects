def spy_game(mylist):#[1,2,4,0,0,7,5]
    list1 = []
    for i in mylist:
        if i == 0 or i == 7:
            list1.append(i)
    if list1[0] == 0 and list1[1] == 0 and list1[2] == 7:
        return True
    else:
        return False

print(spy_game([1,7,2,0,4,5,0]))
