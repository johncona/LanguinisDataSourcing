# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 19:08:22 2015 @author: Andrew
"""

import hashlib
import urllib
import urllib2
import time
import pandas as pd
try:
    import json
except ImportError:
    import simplejson as json

class Mixpanel(object):

    ENDPOINT = 'https://mixpanel.com/api/'
    VERSION = '2.0'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def request(self, methods, params, format='json'):
        """
            methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
                      will give us http://mixpanel.com/api/2.0/events/properties/values/
            params - Extra parameters associated with method
        """
        params['api_key'] = self.api_key
        params['expire'] = int(time.time()) + 600   # Grant this request 10 minutes.
        params['format'] = format
        if 'sig' in params: del params['sig']
        params['sig'] = self.hash_args(params)

        request_url = '/'.join([self.ENDPOINT, str(self.VERSION)] + methods) + '/?' + self.unicode_urlencode(params)

        request = urllib2.urlopen(request_url, timeout=120)
        data = request.read()

        return json.loads(data)

    def unicode_urlencode(self, params):
        """
            Convert lists to JSON encoded strings, and correctly handle any
            unicode URL parameters.
        """
        if isinstance(params, dict):
            params = params.items()
        for i, param in enumerate(params):
            if isinstance(param[1], list):
                params[i] = (param[0], json.dumps(param[1]),)

        return urllib.urlencode(
            [(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params]
        )

    def hash_args(self, args, secret=None):
        """
            Hashes arguments by joining key=value pairs, appending a secret, and
            then taking the MD5 hex digest.
        """
        for a in args:
            if isinstance(args[a], list): args[a] = json.dumps(args[a])

        args_joined = ''
        for a in sorted(args.keys()):
            if isinstance(a, unicode):
                args_joined += a.encode('utf-8')
            else:
                args_joined += str(a)

            args_joined += '='

            if isinstance(args[a], unicode):
                args_joined += args[a].encode('utf-8')
            else:
                args_joined += str(args[a])

        hash = hashlib.md5(args_joined)

        if secret:
            hash.update(secret)
        elif self.api_secret:
            hash.update(self.api_secret)
        return hash.hexdigest()

if __name__ == '__main__':
    api = Mixpanel(
        api_key = "122d4943394fb9d73f00c8a4b7e69723",
        api_secret = "68d1c606da4b0e3180b6907b85092ab1"
    )
    data = api.request(['events'], {
        'event' : ['Install', 'First Time Launch','User: Facebook Login','User: New Session', 'Tutorial Completion Event', 'Sent Crash Log', 'Liked Game', 'Facebook Request Sent','Facebook Request Failed', 'Collected Daily Reward','IAP: Buy 10 Coins Success', 'IAP: Buy 20 Coins Success','IAP: Buy 55 Coins Success','IAP: Buy 110 Coins Success','IAP: Buy 220 Coins Success','IAP: Buy 560 Coins Success','IAP: Buy Unlock Gate Success'],
        'unit' : 'day',
        'interval' : 30,
        'type': 'unique'
    })
    print data['data']['values']
