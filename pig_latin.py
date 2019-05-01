word = input('Enter a word: ')

def pig_latin(str):
    first_letter = str[0]
    if first_letter in 'aeiou':
        return str + 'ay'
    else:
        new_word = str[1:]
        return new_word + first_letter + 'ay'

print(pig_latin(word))
