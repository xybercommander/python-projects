sentence = input()
mylist = list(sentence)

for i in range(len(mylist)):
    if i%2 == 0:
        mylist[i] = mylist[i].lower()
    else:
        mylist[i] = mylist[i].upper()

funny_sentence = ''.join(mylist)
print(funny_sentence)
