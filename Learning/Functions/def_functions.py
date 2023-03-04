def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False


#----------------------------


def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)

function(3)
function(5, ['a', 'b', 'c'])
function(6)


#----------------------------


def is_distinct(items):
    return len(items) == len(set(items))


#----------------------------


def remove_duplicates(x):
    return list(set(x))


#----------------------------


def count_str1(x):
    s = 0
    for i in x:
        if isinstance(i, str) and len(i) > 2:
            s += 1
    return s


#----------------------------


def count_str(x):
    s = 0
    for i in x:
        if isinstance(i, str):
            s += 1
    return s


#----------------------------


def filter_ge_6(lista):
    x = []
    for i in lista:
        if len(i) >= 6:
            x.append(i)
    return x


#----------------------------


def map_longest(lista):
    x = []
    for i in lista:
        x.append(len(i))
        return max(x)


#----------------------------


def multi(x):
    y = 1
    if isinstance(x, list) or isinstance(x, tuple):
        for i in x:
            y *= int(i)
        return y


#----------------------------


def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


#----------------------------


def maximum(x, y):
    if x >= y:
        return x
    else:
        return y
