
from math import sqrt

def sieveOfEratosthenes(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            print(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)

    
def main():
    sieveOfEratosthenes(35)

    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()