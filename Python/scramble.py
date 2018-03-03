
import sys

def string_scramble(string_one, string_two):
    list1 = list(string_one.lower())
    list2 = list(string_two.lower())
    result = []
    
    for chr in list1:
        if chr in list2 and chr not in result: result.append(chr)
    
    return result
    
def main():
    print(string_scramble('GraSS', 'grilled cheese'))

    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()