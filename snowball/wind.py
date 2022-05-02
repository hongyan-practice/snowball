#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2022/5/2'
__author__ = 'sparrow'

import json
import requests

from typing import Union, List


class wind(object):
    def __init__(self, front_url="150.158.140.29"):
        self.headers = {
            'User-Agent': 'snowballsdk/1.0.0'
        }
        self.url = "http://" + front_url + ":8080/wsd"

    def wsd(self, codes: Union[str, List[str]], fields: Union[str, List[str]], beginTime: str, endTime: str,
            options: str):
        """
        获取日时间序列函数

        参考：https://www.windquant.com/qntcloud/apiRefHelp/id-91573a98-70d5-4462-8c6f-546ab45c8652
        :return:
        """
        payload = {}
        payload["codes"] = codes
        payload["fields"] = fields
        payload["beginTime"] = beginTime
        payload["endTime"] = endTime
        payload["options"] = options
        response = requests.post(url=self.url, headers=self.headers, data=payload, timeout=30)
        if response.status_code == 200:
            content = json.loads(response.content)
            return content
        else:
            raise Exception("获取日时间序列函数失败 (%d,%s)" % (response.status_code, json.loads(response.content)))
