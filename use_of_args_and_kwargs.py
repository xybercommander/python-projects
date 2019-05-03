def func(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

func(10,20,30,fruit = 'apple',food = 'eggs',animal = 'cat')
