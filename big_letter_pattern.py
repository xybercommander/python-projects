def print_big(letter):
    patterns = {
        1:'*****',
        2:'**** ',
        3:'***  ',
        4:'**   ',
        5:'*    ',
        6:'  *  ',
        7:' * * ',
        8:'*   *',
        9:'* *  ',
        10:'*  * ',
    }
    alphabet = {
        'A':[6,7,1,8,8],
        'B':[9,10,4,10,9]
    }
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('b')
#well technically make more letters but i am lazy
