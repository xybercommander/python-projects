def myfunc(str):
    output = []
    for i in range(len(str)):
        if i%2 == 0:
            output.append(str[i].upper())
        else:
            output.append(str[i].lower())
    return ''.join(output)

print(myfunc('samrat'))
