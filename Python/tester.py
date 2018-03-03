
import sys

def rpn(equation):
    ops = [ '+', '-', '*', '/' ]
    tokens = equation.split()
    stack = []
   
    #print(tokens)
    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            if token == '+':
                result = arg1 + arg2
            elif token == '-':
                result = arg1 - arg2
            elif token == '*':
                result = arg1 * arg2
            elif token == '/':
                result = arg1 / arg2
            stack.append(result)
        else:
            #print(token)
            stack.append(int(token))
   
    return stack.pop()
    
def main():
    #print(rpn('3 4 +'))
    #print(rpn('4 2 /'))
    print(rpn('15 7 1 1 + - / 3 * 2 1 1 + + -'))

    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()