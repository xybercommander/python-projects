word = input('Enter a word: ')

def pig_latin(str):
    first_letter = str[0]
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u':
        return str + 'ay'
    else:
        new_word = str[1:]
        return new_word + first_letter + 'ay'

print(pig_latin(word))
