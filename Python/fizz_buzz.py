# import sys


def fizz_buzz(x):
    for num in range(1, x+1):
        div3 = num % 3 == 0
        div5 = num % 5 == 0
        if div3 and div5:
            print('FizzBuzz')
        elif div3:
            print('Fizz')
        elif div5:
            print('Buzz')
        else:
            print(num)


# Define a main() function 
def main():
    fizz_buzz(20)
        
    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()