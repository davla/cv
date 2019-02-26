#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial
from os import listdir, path

import yaml
from flask import Flask, render_template

from lib.filters import add_filters

app = Flask(__name__)

app.jinja_options = dict(app.jinja_options,
                         lstrip_blocks=True,
                         trim_blocks=True)
add_filters(app)


def cv_endpoint(jinja_path, template_name):
    with open('info.yaml') as info_file:
        data = yaml.load(info_file)
    return render_template(jinja_path, css=template_name, **data)


cv_dir = path.join(app.root_path, app.template_folder, 'templates')

for cv_file in listdir(cv_dir):
    cv_name = path.splitext(cv_file)[0]
    cv_jinja_path = path.join('templates', cv_file)
    cv_url = '/templates/{}'.format(cv_name)

    app.add_url_rule(cv_url, cv_name,
                     partial(cv_endpoint, cv_jinja_path, cv_name))

if __name__ == '__main__':
    app.run(debug=True)
