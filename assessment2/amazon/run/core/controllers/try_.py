#!/usr/bin/env python3

from flask import Blueprint, Flask, render_template, request, url_for

controller = Blueprint('try_', __name__, url_prefix='/try_')


# @controller.route('/<string:title>', methods=['GET'])
# def lookup(title):
#     if title == 'Republic':  # TODO 2
#         return render_template('republic.html')  # TODO 2
#     else:
#         pass
