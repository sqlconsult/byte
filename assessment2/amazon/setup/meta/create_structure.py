#!/usr/bin/env python3

import csv


def get_namespaces():
    ret_names = []
    with open('namespace.txt', 'r') as f:
        rows = csv.reader(f)

        # write a controller for each namespace (books, toys, etc)
        for row in rows:
            ret_names.append(row[0])

    return sorted(ret_names)


def main():
    path = '/home/steve/byte/assessment2/amazon/run/core/'
    names = get_namespaces()
    template_filename = path + 'templates/structure.html'

    # write structure.html files
    with open(template_filename, 'w+') as out:
        out.write('<!DOCTYPE html>\n')
        out.write('<html lang="en">\n')
        out.write('<head>\n')
        out.write('    <meta charset="UTF-8">\n')
        out.write('    <title>Steves Shop</title>\n')
        out.write('</head>\n')
        out.write('<body>\n')
        out.write('    <h1>Steves Shop</h1>\n')
        out.write('    <form action="/structure/router" method="post">\n')
        out.write('        <h3>Department:</h3>\n')
        out.write('        <select name="select_department" >\n')
        out.write('            <option selected="selected" value="none">Select an option…</option>\n')

        for name in names:
            out_line = '            <option value="{name}">{name}</option>\n'.format(name=name)
            out.write(out_line)

        out.write('        </select>\n')
        out.write('        <button type="submit" class="btn btn-default">Go</button>\n')
        out.write('    </form>\n')
        out.write('    {% block main %}\n')
        out.write('    {% endblock main %}\n')
        out.write('</body>\n')
        out.write('</html>\n')


if __name__ == '__main__':
    main()