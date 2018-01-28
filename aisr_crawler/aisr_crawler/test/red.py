# this is use python script!
# -*- coding: UTF-8 -*-

import urllib
from urllib import request

class JDRedirectHandler(request.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        result = request.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        return result;