#!/usr/bin/env python3
# import json
import os
# import time

from flask import Flask, render_template, request

from core.controllers.trader import controller as traders

# import logging
# from logging.handlers import RotatingFileHandler


omnibus = Flask(__name__)
omnibus.register_blueprint(traders)


# # initialize the log handler
# logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
# formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
# logHandler.setFormatter(formatter)
#
# # set the log handler level
# logHandler.setLevel(logging.INFO)
#
# # set the app logger level
# omnibus.logger.setLevel(logging.INFO)
# omnibus.logger.addHandler(logHandler)


# TODO 1	Finish this function
#   write the logic to create a key that will sign cookies


def keymaker(omnibus, filename='secret_key'):
    # omnibus.logger.info('Enter keymaker')
    # Does the file secret_key exist in this directory?
    filename = os.path.join(omnibus.instance_path, filename)
    try:
        # Yes, read it and get the key
        # omnibus.logger.info('secret key exists, read from file')
        omnibus.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        # omnibus.logger.warning('secret key does not exist, will create it')
        # No, get the path and create & populate it
        absolute_path = os.path.dirname(filename)
        if not os.path.isdir(absolute_path):
            os.system('mkdir -p {absolute_path}'.format(absolute_path=absolute_path))
        os.system('head -c 24 /dev/urandom > {filename}'.format(filename=filename))


keymaker(omnibus)
