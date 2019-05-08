#Program to reverse the words of a sentence
#Hello World --> World Hello

def master_yoda(text):
    list1 = text.split()
    new_sentence = ' '.join(list1[::-1])
    return new_sentence

print(master_yoda('Hello World'))
