# -*- coding:utf-8 -*-
# @Author: clark
# @Time: 2021/5/26 5:53 下午
# @File: demo_1.py
# @project demand:
import requests

headers = {
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://deal.ggzy.gov.cn',
    'Referer': 'http://deal.ggzy.gov.cn/ds/deal/dealList.jsp',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

data = {
    # 'TIMEBEGIN_SHOW': '2021-03-24',
    # 'TIMEEND_SHOW': '2021-04-02',
    # 'TIMEBEGIN': '2021-03-24',
    # 'TIMEEND': '2021-04-02',
    'SOURCE_TYPE': '1',
    'DEAL_TIME': '02',
    'DEAL_CLASSIFY': '00',
    'DEAL_STAGE': '0000',
    'DEAL_PROVINCE': '0',
    'DEAL_CITY': '0',
    'DEAL_PLATFORM': '0',
    'BID_PLATFORM': '0',
    'DEAL_TRADE': '0',
    'isShowAll': '1',
    'PAGENUMBER': '8181',
    'FINDTXT': ''
}

response = requests.post('http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp',
                         headers=headers,
                         data=data,
                         verify=False,
                         )
from pprint import pprint

pprint(response.json())
