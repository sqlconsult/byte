import fractions
import math

def compute_divisors(num):
    retVal = []

    # upper limit = sqrt(num) because if the two factors are the same,
    # they're both the square root. If you make one factor bigger,
    # you have to make the other factor smaller. This means that one
    # of the two will always be less than or equal to sqrt(x), so
    # you only have to search up to that point to find one of the
    # two matching factors. 

    upper_limit = int(math.sqrt(num))+1

    for i in range(1, upper_limit):
        if num % i == 0:
            retVal.append(i)
            retVal.append(int(num/i))
    return retVal

def sum_of_divisors(num):
    divs = compute_divisors(num)
    total = sum(divs)
    return total

def divisor_count(num):
    divs = compute_divisors(num)
    cnt = len(divs)
    return cnt

def get_totatives(num):
    # initialize return value
    tot_list = []

    # loop over all numbers < input value
    for i in range(1, num+1):

        # Return greatest common divisor (gcd) of the integers i and num
        gcd = fractions.gcd(i,num)

        # if gcd = 1 then this is a totative, append it to the list
        if gcd == 1:
            tot_list.append(i)

    return tot_list

def totient(num):
    # totient = sum(totatives(num))
    return sum(get_totatives(num))

inp_num = 30
print('Number: ', str(inp_num))
print('   Divisors: ', compute_divisors(inp_num))
print('   Sum of Divisors: ', sum_of_divisors(inp_num))
print('   Divisor Couunt: ', divisor_count(inp_num))
print('   Totatives: ', get_totatives(inp_num))
print('   Totient: ', totient(inp_num))
