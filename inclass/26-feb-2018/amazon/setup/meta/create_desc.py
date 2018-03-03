#!/usr/bin/env python3

import csv
import os


def get_namespaces():
    ret_names = []
    with open('namespace.txt', 'r') as f:
        rows = csv.reader(f)

        # write a controller for each namespace (books, toys, etc)
        for row in rows:
            ret_names.append(row[0])

    return sorted(ret_names)


def main():
    path = '/home/steve/byte/inclass_sg/26-feb-2018/amazon/run/core/'

    names = get_namespaces()

    # write a controller for each namespace (books, toys, etc)
    for name in names:
        # if description directory exists, delete it
        name_desc_dir = path + 'descriptions/{name}/'.format(name=name)

        # print(name_desc_dir)
        if os.path.exists(name_desc_dir) and os.path.isdir(name_desc_dir):
            os.system("rm -rf " + name_desc_dir)

        os.makedirs(name_desc_dir)

        # create 5 dummy image files in for each department
        for num in range(5):
            desc_filename = name_desc_dir + '{name}_desc_{num}.txt'.\
                format(name=name, num=num)

            with open(desc_filename, 'w+') as out:
                out.write('This is a dynamically added list item - {name} {num}'.
                          format(name=name, num=num))


if __name__ == '__main__':
    main()