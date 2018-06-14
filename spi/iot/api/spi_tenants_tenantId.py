# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class SpiTenantsTenantid(Resource):

    def get(self, tenantId):

        return None, 200, None

    def delete(self, tenantId):

        return None, 200, None