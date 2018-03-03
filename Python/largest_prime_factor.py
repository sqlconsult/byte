
from math import sqrt

def largest_prime_factor(num):
    div=2
    while div < num:
        print('div=', div,'num=',num)
        if num % div == 0 and num/div > 1:
            num = num /div
            div = 2
        else:
            div = div + 1
    return num
    
def main():
    print(largest_prime_factor(15))
    #print(largest_prime_factor(18))
    #print(largest_prime_factor(19))

    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()