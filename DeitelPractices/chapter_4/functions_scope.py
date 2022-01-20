x = 7


def access_global():
    print('global x is', x)


def try_to_modify_global():
    x = 3.5
    print('local x is', x)


access_global()
try_to_modify_global()
print(x)


def changing_x():
    global x
    x = 'babe'


changing_x()
print(x)