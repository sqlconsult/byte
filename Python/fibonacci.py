import sys


def fibonacci(num):
    if num >= 2:
        print('0')
        print('1')
        prev1 = 1
        prev2 = 0
        newsum = 1
        while newsum < num:            
            print(newsum)
            prev2=prev1
            prev1=newsum
            newsum=prev1+prev2
    elif num == 1:
        print('0')
    

def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)


# Define a main() function 
def main():
    # fibonacci(7)
    for num in range(0, 7 + 1):
        print(F(num))

    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
