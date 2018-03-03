import sys


def cat(filename):
    f = open(filename, 'rU')
    for line in f:
        print(line, end=' ')  # trailing comma inhibits printiing new line
    f.close()


# Define a main() function that prints a little greeting
def main():
    cat(sys.argv[1])


# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
