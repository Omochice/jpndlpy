#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' JapanNdlClientBase
Python wrapper for Japan National Dict Library API
Details: http://iss.ndl.go.jp/information/api/
created by @shimakaze-git
'''

import requests
from requests import RequestException

from exceptions import JapanNdlException
from response import JapanNdlResponse
# ''' qiita.QiitaClientBase
# Base for QiitaClient
# Implements some primitive methods for request Qiita API v2
# created by @petitviolet
# '''
# import requests
# import yaml
# from .exception import QiitaApiException
# from .response import QiitaResponse


class JapanNdlClientBase:

    HOST = 'iss.ndl.go.jp/api/opensearch'
    ACCEPT = 'application/json'

    @property
    def api_url(self):
        return 'https://{}?'.format(self.HOST)

    def _request(self, url, params=None):
        ''' requests process
        '''
        method = "GET"
        response = requests.request(
            method=method, url=url, params=params
        )

        if response.ok:
            return JapanNdlResponse(response)
        else:
            return JapanNdlException(response)

    def request(self, params=None):
        url = self.api_url
        return self._request(url, params)

    def get(self, params=None):
        ''' get request
        >>> client.get('/users/petitviolet').status
        200
        '''
        return self.request(params)

    def serializer(self, params, **kwargs):
        ''' serializer url
        paramsの中のURLをシリアライズする
        Parameters
        ----------
        params : dict
            GETパラメーターが格納された辞書
        '''
        serializer_params = ''.join([
            p+"="+str(params[p])+"&" for p in params
        ])

        """
        以下にシリアライズ

        from_date -> from
        until_date -> until
        """
        serializer_params = serializer_params.replace(
            'from_date=',
            'from='
        )
        serializer_params = serializer_params.replace(
            'until_date=',
            'until='
        )
        return serializer_params
