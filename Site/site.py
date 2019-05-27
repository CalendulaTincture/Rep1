#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route("/")
def root():
    return flask.render_template(
        'index.html'
    )


@app.route("/calc", methods=['GET'])
def calc():
    if request.method == 'GET':
        num1 = request.args.get('number1')
        num2 = request.args.get('number2')
        opr = request.args.get('operation')

    elif request.method == 'POST':
        name_param = request.form.get('number1', 'number2', 'operation')

    if num1 == None:
        num1 = 0
    if num2 == None:
        num2 = 0
    if opr == None:
        opr = '+'

    num1, num2, opr = int(num1), int(num2), str(opr)

    if opr == '+':
        res = num1+num2
    elif opr == '-':
        res = num1-num2
    elif opr == '*':
        res = num1*num2
    elif opr == '/':
        res = num1/num2
    elif opr == '^':
        res = num1**num2

    return flask.render_template(
        'calculator.html',
        res=res,
        num1=num1,
        num2=num2,
        opr=opr,
        method=request.method
    )


if __name__ == '__main__':
    app.run(debug=True)
