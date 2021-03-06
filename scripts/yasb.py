#!/usr/bin/env python2.7

# Copyright (c) 2015- Peter Bui <peter.j.bui@gmail.com>

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

""" Yet Another Static Blogger """

import collections
import itertools
import sys

import dateutil.parser
import tornado.template
import markdown
import markdown.extensions.codehilite
import yaml

# Page -------------------------------------------------------------------------

PageFields = 'title prefix icon navigation internal external body'.split()
Page       = collections.namedtuple('Page', PageFields)

def load_page_from_yaml(path):
    data     = yaml.load(open(path))
    external = data.get('external', {}) or {}

    for k, v in external.items():
        data['external'][k] = yaml.load(open(v))

    if 'prefix' not in data:
        data['prefix'] = '/~cforstal/cdt-30020-sp17/'

    return Page(**data)

def render_page(page):
    hilite = markdown.extensions.codehilite.CodeHiliteExtension(noclasses=True)
    loader = tornado.template.Loader('templates')
    layout = '''
{{% extends "base.tmpl %}}

{{% block body %}}
{}
{{% end %}}
'''.format(markdown.markdown(page.body, extensions=['extra', hilite]))

    template = tornado.template.Template(layout, loader=loader)
    settings = {
        'page'      : page,
        'dateutil'  : dateutil,
        'itertools' : itertools,
    }
    return template.generate(**settings).decode('utf-8')

# Main Execution ---------------------------------------------------------------

if __name__ == '__main__':
    for path in sys.argv[1:]:
        page = load_page_from_yaml(path)
        print render_page(page)

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
