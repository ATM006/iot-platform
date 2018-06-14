# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import iot


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        iot.bp,
        url_prefix='/iot')
    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0',port=8081,debug=True)
