#!/usr/bin/env python3

import json
import os
import time

from flask import(
                   Flask,
                   jsonify,
                   render_template,
                   request,
                   url_for)

# from core.extend import authorize
from core.endpoints.controller_1 import controller as cryptocurrencies


def keymaker(omnibus, filename='secret_key'):
    filename = os.path.join(omnibus.instance_path(filename))
    try:
        omnibus.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        absolute_path = os.path.dirname(filename)
        if not os.path.isdir(absolute_path):
            os.system('mkdir -p {absolute_path}'.format(absolute_path=absolute_path))
        os.system('head -c 24 /dev/urandom > {filename}'.format(filename=filename))


omnibus = Flask(__name__)
omnibus.register_blueprint(cryptocurrencies)

keymaker(omnibus)
