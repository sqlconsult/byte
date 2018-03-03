#!/usr/bin/env python3

import os
from flask import Blueprint, Flask, render_template, request

from core.controllers.books import controller as books
from core.controllers.electronics import controller as electronics
from core.controllers.movies import controller as movies
from core.controllers.home import controller as home
from core.controllers.food import controller as food
from core.controllers.beauty import controller as beauty
from core.controllers.toys import controller as toys
from core.controllers.clothing import controller as clothing
from core.controllers.handmade import controller as handmade
from core.controllers.sports import controller as sports
from core.controllers.automotive import controller as automotive
from core.controllers.structure import controller as structure
# import logging
# from logging.handlers import RotatingFileHandler


def key_maker(filename='secret_key'):
    filename = os.path.join(omnibus.instance_path, filename)
    try:
        omnibus.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        absolute_path = os.path.dirname(filename)
        if not os.path.isdir(absolute_path):
            os.system('mkdir -p {absolute_path}'.format(absolute_path=absolute_path))
        os.system('head -c 24 /dev/urandom > {filename}'.format(filename=filename))

    omnibus.config['SECRET_KEY'] = open(filename, 'rb').read()


omnibus = Flask(__name__)
omnibus.register_blueprint(books)
omnibus.register_blueprint(electronics)
omnibus.register_blueprint(movies)
omnibus.register_blueprint(home)
omnibus.register_blueprint(food)
omnibus.register_blueprint(beauty)
omnibus.register_blueprint(toys)
omnibus.register_blueprint(clothing)
omnibus.register_blueprint(handmade)
omnibus.register_blueprint(sports)
omnibus.register_blueprint(automotive)
omnibus.register_blueprint(structure)

key_maker()


@omnibus.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        # This is an HTTP get request.
        return render_template('index.html')
