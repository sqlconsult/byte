#!/usr/bin/env pythonn3

from flask import Flask, render_template, request


app = Flask(__name__)

# Flask routing with URI Manipulation
#@app.route('/<int:kenso_says>', methods=['GET'])
#def grandpa_1(kenso_says):
#    if request.method == 'GET':
#        # this is an HTTP get request#
#         print(kenso_says)    # print results appear on Terminal
#        return render_template('index.html')


#@app.route('/<string:class_says>', methods=['GET'])#
#def grandpa(class_says):
#    if class_says == class_says.upper():
#        return render_template('index.html', message='I can hear you now.  Get off my lawn')
#    else:
#        return render_template('index.html', message='I can\'t hear you')


# HTML Form Fields
@app.route('/', methods=['GET', 'POST'])
def grandpa():
    if request.method == 'GET':
        return render_template('index.html', message='some text message')
    else:
        class_says = request.form['classsays']
        if class_says == class_says.upper():
            return render_template('index.html', message='I can hear you now.  Get off my lawn')
        else:
            return render_template('index.html', message='I can\'t hear you')


if __name__ == '__main__':
    app.run(debug=True)
