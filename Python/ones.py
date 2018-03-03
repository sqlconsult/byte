#!/bin/python3

import sys

def longest_consecutive_one(n):
    stack = []
    counter = 0
    binary_num = '{0:08b}'.format(n)
    # print(binary_num)
    
    length = len(binary_num) - 1
    
    #  enumerate() function adds a counter to an iterable. 
    # So for each element in cursor , a tuple is produced with (counter, element) 
    for index, character in enumerate(binary_num):
        if character == "1":
            # increment count of 1's
            counter += 1
        if character == '0' or index == length:
            # add this count to list of consecutive one counts
            stack.append(counter)
            counter = 0
    return max(stack)
    

inp = input('Input number: ')
n = int(inp.strip())
retVal = longest_consecutive_one(n)
print(retVal)