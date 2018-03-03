#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, request

import model
import view

app = Flask(__name__)

@app.route('/', methods=['GET'])

def show_menu():
    x = view.actually_show_menu()
    return render_template('dashboard.html')

# this is an example of a Flask route
@app.route('/', methods=['GET','POST']
def frontpage():
    if request.method == 'GET':
        # this is a get request
        return render_template('index.html')
    else:
        # this is a post request
        user_name = request.form['username']
        password  = request.form['password']
        print(user_name, password)
        return

if __name __ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=true)
