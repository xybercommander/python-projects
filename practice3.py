def paper_doll(text):
    list1 = list(text)
    for i in range(len(list1)):
        list1[i] = list1[i]*3
    new_word = ''.join(list1)
    return new_word

print(paper_doll('Hello'))
