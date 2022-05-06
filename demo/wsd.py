#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2022/5/6'
import pandas as pd

"""
tiny demo 
- 需要安装 pandas: pip install pandas
- 安装包: pip install ./snowball-0.0.1-py3-none-any.whl
"""

# 创建 wind 实例, front_url 为 wind 前置机地址，即登录 wind 客户端的地址.
w = wind(front_url="150.158.140.29")
# 调用接口 wsd
# 需要检测返回值，当返回值为 0 时，说明请求正确，可以获取到正确的 dataframe
r = w.wsd("510050.SH", "close,OPEN,pct_chg", "2022-03-01", "2022-05-1", "unit=1")
code = r["errorCode"]
if not code:
    df = pd.read_json(r["data"])
    print(df.to_string())
else:
    print(f'请求错误，请检查输入参数, 错误信息{r["data"]}.')
