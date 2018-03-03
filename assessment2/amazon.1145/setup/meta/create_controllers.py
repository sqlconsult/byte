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

    # write a controller for each namespace (books, toys, etc)
    for name in names:
        controller_filename = path + 'controllers/{file_nm}.py'.format(file_nm=name)

        with open(controller_filename, 'w+') as out:
            out.write("#!/usr/bin/env python3\n\n")
            out.write("from flask import Blueprint, Flask, render_template, request, url_for\n\n")
            out.write("controller = Blueprint('{stem}', __name__, url_prefix='/{stem}')\n\n\n".format(stem=name))
            out.write("# @controller.route('/<string:title>', methods=['GET'])\n")
            out.write("# def lookup(title):\n")
            out.write("#     if title == 'Republic':  # TODO 2\n")
            out.write("#         return render_template('republic.html')  # TODO 2\n")
            out.write("#     else:\n")
            out.write("#         pass\n")

    # write html files
    for name in names:
        template_filename = path + 'templates/{file_nm}.html'.format(file_nm=name)

        # print(template_filename)
        with open(template_filename, 'w+') as out:
            out.write('{% extends "structure.html" %}\n')
            out.write('{% block main %}\n')
            out.write('<h1> This is an H1 Header - {stem} </h1>\n'.format(stem=name))
            out.write('<br>\n')
            out.write('<ul>\n')
            out.write('{% for item in items %}\n')
            out.write('    <li>{{ item }}</li>\n')
            out.write('{% endfor %}\n')
            out.write('</ul>\n')
            out.write('<br>\n')
            out.write('{% endblock main %}\n')


if __name__ == '__main__':
    main()
