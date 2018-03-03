def binary_to_decimal(num):
    # convert binary string to array of 1's and 0's
    nums = list(num)

    # begin with exponenet = 0, 2**0
    exp = 0

    # keep running total
    total = 0

    # loop over input string in reverse order
    for i in range(len(nums) - 1, -1, -1):
        # conpute the value of this digit
        value = int(nums[i]) * 2 ** exp
        # increment total by value of this digit
        total += value
        # increase exponent for next digit
        exp += 1

    return total

def x_decimal_to_binary(num):

    # using loops
    binary = ''

    while (num):
        if num % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        num = num // 2    # // = floor division

    result = ''.join(reversed(binary))
    return result


def decimal_to_binary(num):
    if num < 0:
        return 'Must be a positive integer'
    elif num == 0:
        return '0'
    else:
        return decimal_to_binary(num // 2) + str(num % 2)


def main():
    exit_loop = False

    while not exit_loop:
        action = input('Enter 1 to convert binary to decimal or 2 to convert decimal to binary: ')
        inp_val = input('Enter number to convert: ')
        if action == '1':
            result = binary_to_decimal(inp_val)
            print(inp_val + ' converted to decimal = ' + str(result))
        elif action == '2':
            num = int(inp_val)
            result = decimal_to_binary(num)
            print(inp_val + ' converted to binary = ' + result[1:])
        else:
            exit_loop = True


if __name__ == '__main__':
    main()
