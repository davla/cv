#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
import re
import sys

import jinja2
from markupsafe import Markup

multi_newline = re.compile(r'(?:\n|\r|\r\n){2,}')


@jinja2.evalcontextfilter
def nl2br(eval_ctx, value):
    paragraphs = multi_newline.split(jinja2.escape(value))
    ps = ('<p>{}</p>'.format(p.replace('\n', Markup('<br>\n')))
          for p in paragraphs)
    result = '\n\n'.join(ps)

    if eval_ctx.autoescape:
        result = Markup(result)

    return result


jinja_filters = inspect.getmembers(sys.modules[__name__], inspect.isfunction)


def add_filters(app):
    for name, jinja_filter in jinja_filters:
        app.jinja_env.filters[name] = jinja_filter
