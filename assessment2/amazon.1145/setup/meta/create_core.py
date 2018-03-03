#!/usr/bin/env python3

import os
import csv


# TODO create __init__.py with the following
#
# # import json
# import os
# # import time
#
# from flask import Flask, render_template
#
# from core.controllers.books import controller as books
#
# import logging
# from logging.handlers import RotatingFileHandler
#
#
# omnibus = Flask(__name__)
# omnibus.register_blueprint(books)
# omnibus.register_blueprint(electronics)
# omnibus.register_blueprint(movies)
# omnibus.register_blueprint(home)
# omnibus.register_blueprint(food)
# omnibus.register_blueprint(beauty)
# omnibus.register_blueprint(toys)
# omnibus.register_blueprint(clothing)
# omnibus.register_blueprint(handmade)
# omnibus.register_blueprint(sports)
# omnibus.register_blueprint(automotive)
#
#
# # initialize the log handler
# logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
# formatter = logging.Formatter(
#         "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
# logHandler.setFormatter(formatter)
#
# # set the log handler level
# logHandler.setLevel(logging.INFO)
#
# # set the app logger level
# omnibus.logger.setLevel(logging.INFO)
# omnibus.logger.addHandler(logHandler)
#
#
# # TODO 1	Finish this function
# #   write the logic to create a key that will sign cookies
#
#
# def keymaker(omnibus, filename='secret_key'):
#     omnibus.logger.info('Enter keymaker')
#     # Does the file secret_key exist in this directory?
#     filename = os.path.join(omnibus.instance_path, filename)
#     try:
#         # Yes, read it and get the key
#         omnibus.logger.info('secret key exists, read from file')
#         omnibus.config['SECRET_KEY'] = open(filename, 'rb').read()
#     except IOError:
#         omnibus.logger.warning('secret key does not exist, will create it')
#         # No, get the path and create & populate it
#         absolute_path = os.path.dirname(filename)
#         if not os.path.isdir(absolute_path):
#             os.system('mkdir -p {absolute_path}'.format(absolute_path=absolute_path))
#         os.system('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
#
#
# keymaker(omnibus)
#
#
# @omnibus.route('/', methods=['GET'])
# def homepage():
#     return render_template('index.html')

file_nm = '__init__.py'

path = '/home/steve/byte/assessment2/amazon/'

filename = path + 'run/core/{file_nm}'.format(file_nm=file_nm)

with open(filename, 'w') as out:
    out.write('#!/usr/bin/env python3\n')
    out.write('\n')
    out.write('import os\n')
    out.write('from flask import Blueprint, Flask, render_template, request\n')

    with open('namespace.txt', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            out.write('from core.controllers.{stem} import controller as {stem}\n'.
                      format(stem=row[0]))
    out.write('from core.controllers.structure import controller as structure\n')

    out.write('# import logging\n')
    out.write('# from logging.handlers import RotatingFileHandler\n')
    out.write('\n\n')

    out.write('omnibus = Flask(__name__)\n')
    out.write('\n')

    with open('namespace.txt', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            out.write('omnibus.register_blueprint({stem})\n'.format(stem=row[0]))
    out.write('omnibus.register_blueprint(structure)\n')
    out.write('\n\n')
    out.write("@omnibus.route('/', methods=['GET'])\n")
    out.write("def home_page():\n")
    out.write("    if request.method == 'GET':\n")
    out.write("        # This is an HTTP get request.\n")
    out.write("        return render_template('index.html')\n")
