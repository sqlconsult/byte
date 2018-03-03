import math
import sys

def mySqrt(value, tolrnc):
    start = 0
    end = value
    mid = (end + start) / 2
  
    
    loopCntr = 0
    
    while abs(mid*mid - value) > tolrnc:
        msg = str(loopCntr) + ': '
        print(msg, start, mid, end)
        if mid*mid > value:
            end = mid
        else:
            start = mid

        mid = (end + start) / 2
        
        loopCntr += 1
        if loopCntr > 100: break
    return mid



# Define a main() function 
def main():
    value = 10.
    tolrnc = 0.0001
    sqrt = mySqrt( value, tolrnc )  # 3.16227766016837933
    print('sqrt of ', value, ' = ', sqrt)
        
    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()