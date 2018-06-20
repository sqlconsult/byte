#!/usr/bin/env python3


class MyMath():
    def my_div(self, x, y):
        try:
            result = x / y
            return result
        except ZeroDivisionError as ex:
            print('Divide by zero: Exception: [{0}]'.format(ex))
        except TypeError as ex:
            print("Can't convert 'int' object to str implicitly: Exception: [{0}]".format(ex))
        except RuntimeError as ex:
            print("error is detected that doesn’t fall in any of the other categories: Exception: [{0}]".format(ex))


def main():
    obj = MyMath()

    result = obj.my_div(4, 2)
    print('4/2 = {0}'.format(result))

    result = obj.my_div(7, 2)
    print('7/2 = {0}'.format(result))

    result = obj.my_div(1, 0)
    print('1/0 = {0}'.format(result))

    result = obj.my_div('15', 5)
    print('15/5 = {0}'.format(result))


if __name__ == '__main__':
    main()
