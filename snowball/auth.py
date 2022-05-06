#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2022/5/6'

import json
import requests


class auth(object):
    def __init__(self, user_name: str = "", password: str = ""):
        """
        认证类

        Args:
            user_name (str): [必填]账户

            password (str): [必填]账户密码


        Example::

            # 使用实盘帐号直连行情和交易服务器
            from snowball import auth
            auth("用户名", "密码")

        """
        self._user_name = user_name
        self._password = password

    @property
    def _base_headers(self):
        return {
            "User-Agent": "snowball",
            "Authorization": "%s|%s" % (self._user_name, self._password)
        }
