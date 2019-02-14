#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir, path

import yaml
from flask import Flask, render_template

app = Flask(__name__)

cv_templates_dir = path.join(app.root_path, app.template_folder, 'templates')

for cv_template_file in listdir(cv_templates_dir):
    cv_template_name = path.splitext(cv_template_file)[0]
    cv_template_jinja_path = path.join('templates', cv_template_file)


    @app.route('/templates/{}'.format(cv_template_name))
    def cv_template_endpoint():
        with open('info.yaml') as info_file:
            data = yaml.load(info_file)
        return render_template(cv_template_jinja_path, css=cv_template_name,
                               **data)


if __name__ == '__main__':
    app.run(debug=True)
