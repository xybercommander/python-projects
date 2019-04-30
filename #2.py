e = True
print('Welcome to my calculator.................')
print('Developed by Xyber\n\n')
while e == True:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    char = input('Enter + to add, - to substract, * to multiply or / to divide the two numbers: ')
    if char == '+':
        print('The result is: {}'.format(a+b))
    elif char == '-':
        print('The result is: {}'.format(a-b))
    elif char == '*':
        print('The result is: {}'.format(a*b))
    elif char == '/':
        print('The result is: {}'.format(a/b))

    retry = input('Do you want to try again? (y/n) ')
    if retry == 'y':
        continue
    elif retry == 'n':
        e = False
        print('Thank you for using this calculator')
