# -*- coding: utf-8 -*-
import datetime
import os
import unittest

import requests

from util.webHookUtil import notify_by_qywechat

"""
打新可转债
"""


class ApplyNewBondTestCase(unittest.TestCase):
    def test_new_bond_notify(self):
        """
        可转债申购提醒
        :return:
        """
        robot = os.getenv('WEB_HOOK_BOND')
        if robot is None or robot == '':
            print("WEB_HOOK_BOND is empty")
            return
        url = 'http://data.10jqka.com.cn/ipo/kzz/'
        header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'http://data.10jqka.com.cn/ipo/bond/',
            'X-Requested-With': 'XMLHttpRequest',
            'hexin-v': 'AlHxgQkP6kn57gY66HXHGhULZlbovsUnbzJpRDPmTZg32n-Aew7VAP-CeRfA',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        }
        result = requests.request('get', url, headers=header).json()
        self.assertEqual(result['status_code'], 0)
        bonds = result['list']
        template = ""
        today = datetime.date.today()
        # today = datetime.date.fromisoformat('2020-08-20')
        place = "\n"
        for item in bonds:
            sub_date = item['sub_date']
            if today > datetime.date.fromisoformat(sub_date):
                break
            elif today == datetime.date.fromisoformat(sub_date):
                price = item['price']
                expire_date = item['expire_date']
                template += item['bond_code'] + item['bond_name'] + place + \
                            ">正股：" + item['code'] + item['name'] + place + \
                            ">转股价:￥" + price + place + \
                            ">计划发行量:(亿元)" + item['plan_total'] + place + \
                            ">实际发行量:(亿元)" + item['issue_total'] + place + \
                            ">每股获配额:" + item['quota'] + place + \
                            ">到期日:" + expire_date + place + place
        if template == '':
            print('no new bond can be apply today')
            return

        template_title = "新债申购 <font color=\"warning\">{}</font>\n".format(today)
        template_link = "\n[原文](http://data.10jqka.com.cn/ipo/bond/)"
        body = template_title + template + template_link
        robot_result = notify_by_qywechat(robot, body)
        self.assertEqual(robot_result['errcode'], 0)
        return


if __name__ == '__main__':
    unittest.main()
