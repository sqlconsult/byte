import sys

def fahrenheit_to_celsius(temp):
    #  C = (F - 32) * 5/9
    return (temp - 32) * ( 5/9)

def celsius_to_fahrenheit(temp):
    # F = (C * 9/5) + 32.
    return (temp * 9/5) + 32	


# Define a main() function 
def main():
    print(fahrenheit_to_celsius(212))
    print(celsius_to_fahrenheit(0))
        
    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
