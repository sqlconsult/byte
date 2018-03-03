#!/usr/bin/env python3

# using itertools
def iter_tools(inp_str):
    from itertools import permutations
    perms = [''.join(p) for p in permutations(inp_str)]
    return perms



def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    print('string:', string, 'step:', step, 'len(string):', len(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        print('    i:', i, 'string_copy:',       string_copy)
        print('             string_copy[step]:', string_copy[step])
        print('             string_copy[i]:',    string_copy[i])
        print(' ')

        # recurse on the portion of the string that has not been swapped yet (n$
        permutations(string_copy, step + 1)


if __name__ == '__main__':
    print('=' * 25)
    retVal = iter_tools('abc')
    print('retVval:', retVal)
    print('=' * 25)
    permutations('abc')
    print('=' * 25)
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
