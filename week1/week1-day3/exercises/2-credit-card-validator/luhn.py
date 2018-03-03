# c = '4147202086341516'
c = '371757573505001'
#  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
#  4  1  4  7  2  0  2  0  8  6  3  4  1  5  1  6
#
#  8  1  8  7  4  0  4  0 16  6  6  4  2  5  2  6 = 70
#
#  8 + 1 + 8 + 7 + 4 + 0 + 4 + 0 + 1 + 6 + 6 + 6 + 4 + 2 + 5 + 2 + 6 = 70
#

# digits to add as is start at -1 and skip every other character
digits = list(c[-1::-2])

# digits to double start at -2 and skip every other character
digits_to_double = list(c[-2::-2])

# compute sum 
sum = 0

# add individual even position digits to sum
for i in digits:
    sum += int(i)

# double odd position digits and add individual double digit value to sum
# for example: if digit == 4 --> add 8 to sum
#              if digit == 8 --> add 1 + 6 (7) to sum
for i in digits_to_double:
    double = int(i) * 2
    if len(str(double)) > 1:
        s1 = str(double)
        d1 = s1[0]
        d2 = s1[1]
        sum += int(d1) + int(d2)
    else:
        sum += double

print('sum: ', sum)

