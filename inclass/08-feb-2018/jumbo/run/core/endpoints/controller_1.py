#!/usr/bin/env python3

import json
from flask import (
                    Blueprint,
                    jsonify,
                    render_template,
                    request
)

controller = Blueprint('cryptocurrencies', __name__, url_prefix='/exchange/cryptocurrencies')
@controller.route('/', methods = ['GET', 'POST'])
def get_trades():
    with open('datastore/trades.json', 'r') as file:
        trades = json.load(file)['orders']
        if request.method == 'GET':
            payload = request.args
        else:
            payload = request.get_json(silent=True)

# this page will show in localhost:5000/exchange/cryptocurrencies/show-page
@controller.route('/show-page', methods=['GET'])
def show_page():
    return render_template('show-page.html')