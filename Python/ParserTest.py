import argparse
import datetime

def cmdLineParse():
    # python ParserTest.py -h
    # python ParserTest.py
    # python ParserTest.py -sy 1900 -n 15
    # python ParserTest.py --startyear 1976
    # python ParserTest.py --number 12

    # The ArgumentParser object will hold all the information necessary 
    # to parse the command line into Python data types.
    parser = argparse.ArgumentParser(description='Print n leap years starting at StartYear.')

    # Set nargs=1, it will return as a list not a single value
    # Use * to return all parameters if present, or empty list if none
    parser.add_argument('--StartYear', '--startyear', '-sy', required=False, type=int, 
    default=datetime.datetime.now().year,     help='integer starting year (default: current year)')

    parser.add_argument('--Number', '--number', '-n', '-num', required=False, type=int, default=20, 
    help='integer number of leap years to print (default: 20)')
    
    args = parser.parse_args()
    
    print('Args:')
    print('~ Start Year: {}'.format(args.StartYear))
    print('~ Number to print: {}'.format(args.Number))
    return args.StartYear, args.Number

def PrintLeapYear(startYear, num):
    # Initialize leap year counter
    iCnt = 0
    
    # Loop until num leap years found
    while iCnt < num:
        # A leap year has an extra day in it (February 29). That happens every 4 years, 
        # except for years which are both divisible by 100 and not divisible by 400.
        if ((startYear % 4 == 0 and startYear % 100 != 0) or (startYear % 400 == 0)):
            # Increment count of leap years
            iCnt += 1
    
            # Write next leap year
            print('{} {}'.format(iCnt, startYear))
    
        # Next year
        startYear +=1


# Define a main() function 
def main():
    startYear, numToPrint = cmdLineParse()
    PrintLeapYear(startYear, numToPrint)
        
    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()