def main():

    res_words = [ 'and', 'del', 'from', 'not', 'while', 'as', 'elif', 'global', 'or',
                  'with', 'assert', 'else', 'if', 'pass', 'yield', 'break', 'except',
                  'import', 'print', 'class', 'exec', 'in', 'raise', 'continue',
                  'finally', 'is', 'return','def', 'for', 'lambda', 'try',
                  'structure', 'index']

    with open('namespace.txt', 'w+') as f:
        with open('namespace.md', 'r') as g:
            for line in g:
                newline = line[:-1]
                name = newline
                if name in res_words:
                    name = name + '_'
                stem = name.replace('-', '_')
                stem = stem.replace(' ', '_')
                f.write(stem + '\n')


if __name__ == '__main__':
    main()
