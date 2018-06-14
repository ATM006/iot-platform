# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class SpiUsersUsername(Resource):

    def get(self, username):

        return None, 200, None

    def delete(self, username):

        return None, 200, None