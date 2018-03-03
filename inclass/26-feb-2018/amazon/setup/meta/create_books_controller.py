#!/usr/bin/env python3

import os
import csv

# file_nm = '__init.py'
file_nm = 'books_2.py'
path = '/home/steve/byte/inclass_sg/26-feb-2016/amazon/run/core/controllers/'
filename = path + '{file_nm}'.format(file_nm=file_nm)

with open(filename, 'w') as out:
    out.write('#!/usr/bin/env python3\n\n')
    out.write('from flask import Blueprint, render_template\n\n')
    out.write('\n')# TODO 2:	Display multiple books on one page\n\n')
    out.write("controller = Blueprint('books', __name__, url_prefix='/books')\n\n\n")
    out.write("@controller.route('/<string:title>', methods=['GET'])\n")
    out.write('def lookup(title):\n')

    first = True
    with open('books_to_read.txt', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            loc = row[0].find(' by ')
            title = row[0][:loc]
            title = title.replace(' ', '_')
            title = title.replace("'", "_")

            if first:
                out.write("    if title == '{title}':\n".format(title=title))
                first = False
            else:
                out.write("    elif title == '{title}':\n".format(title=title))

            out.write("        return render_template('{title}')\n".format(title=title))

        out.write("    else:\n")
        out.write("        pass\n")
        out.write("        # print('What are you doing')\n")
