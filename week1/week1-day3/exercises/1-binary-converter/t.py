def f(n):
    if n < 0:
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    else:
        return f(n//2) + str(n%2)

n = 16
rslt = f(n)
print('f(' + str(n) + ') = ' + str(rslt[1:]))
