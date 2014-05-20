# -*- coding: utf-8 -*-

# Avoid shadowing the standard library json module
from __future__ import absolute_import
from __future__ import unicode_literals

__author__ = 'Audrey Roy'
__email__ = 'audreyr@gmail.com'
__version__ = '0.1.0'

"""
Serialize data to/from JSON
Inspired by http://git.io/7j9pPg
"""


import datetime
import decimal
import json


def encode_datetime(o):
    r = o.isoformat()
    if o.microsecond:
        r = r[:23] + r[26:]
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r


class JSON262Encoder(json.JSONEncoder):
    """
    JSON encoder aiming to be fully compliant with ECMA-262.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            return encode_datetime(o)
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(JSON262Encoder, self).default(o)
