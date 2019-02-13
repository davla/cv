#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('sidebar/sidebar.jinja',
                           title='sidebar',
                           css='test')


if __name__ == '__main__':
    app.run(debug=True)
