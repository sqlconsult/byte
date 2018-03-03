import sys

def triangle(num):
    for i in range(1, num +1):
        for j in range(1, i+1):
            print('*', end='')
        print()


# Define a main() function 
def main():
    triangle(2)
        
    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
