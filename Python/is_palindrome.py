# import sys


def is_palindrome_rec(string):
    if len(string) < 2:
        print(True)
    if string[0] != string[-1]:
        print(False)
    return is_palindrome(string[1:-1])


def is_palindrome_2(string):
    if string is None or len(string) < 2:
        print(False)
        return

    letters = list(string)
    result = True

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            result = False
            break

    print(result)


def is_palindrome(string):
    # set return value
    result = False

    # leave only letter and numbers in lowercase
    tmp_str = ''.join(e for e in string if e.isalnum())
    tmp_str = tmp_str.lower()

    # make sure its not an empty string
    if tmp_str is not None:
        # reverse string
        test_string = ''.join(reversed(tmp_str))

        # if reverse string same as input string, then its a palindrome
        result = test_string == tmp_str
    return result
    # print('Input string')
    # print(string)
    # print('result')
    # print(result)


# Define a main() function 
def main():
    # is_palindrome('')
    # is_palindrome(None)

    print(is_palindrome('a car, a man, a maraca'))
    print(is_palindrome('kayak'))
    print(is_palindrome('racecar'))

    # is_palindrome('a')
    # is_palindrome('aa')
    # is_palindrome('aaa')
    # is_palindrome('abba')


# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
