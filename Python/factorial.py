# import sys


def factorial(num):
    print('num=', num)
    if num < 2:
        return 1
    return num * factorial(num - 1)


# Define a main() function 
def main():
    print(factorial(5))

    # for f in range(0, 10):
    #    print(f, factorial(f))


# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
