#!/usr/bin/env python3

from flask import Blueprint, Flask, render_template, request, url_for

controller = Blueprint('well_1groomed', __name__, url_prefix='/well_1groomed')


# @controller.route('/<string:title>', methods=['GET'])
# def lookup(title):
#     if title == 'Republic':  # TODO 2
#         return render_template('republic.html')  # TODO 2
#     else:
#         pass
