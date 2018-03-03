#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_frontpage():
    return render_template('index.html')


@app.route('', methods=[])
def():
    return render_template()


if __name__ == '__main__':
    # These parameters are set for a local environment
    app.run(host='127.0.0.1', port=5000, debug=True)

    # These parameters are set for a staging environment
    app.run(host='0.0.0.0', port=5000, debug=True)

    # These parameters are set for a production environment
    app.run(host='0.0.0.0', port=5000, debug=False)
