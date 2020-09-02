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

        template_title = "新债提醒 <font color=\"warning\">{}</font>\n".format(today)
        template_link = "\n[原文](http://data.10jqka.com.cn/ipo/bond/)"
        body = template_title + template + template_link
        robot_result = notify_by_qywechat(robot, body)
        self.assertEqual(robot_result['errcode'], 0)
        return

    # def test_apply_by_xueqiu_pingan(self):
    #     """
    #     todo 因技术局限性，暂时搁置
    #     基于雪球 + 平安
    #     :return:
    #     """
    #     # todo 0 read account from system config
    #     accounts = os.getenv('PINGAN_ACCOUNT')
    #     passwords = os.getenv('PINGAN_PASSWORD')
    #     bot_key = os.getenv('BOT_KEY_QYWECHAT_BOND')
    #
    #     # todo 1 refresh token
    #
    #     # 2 list new bonds
    #     header_list = {
    #         'Cookie: xq_a_token=b05e638b6f7f071b48cef03b79d5c896b035c977;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjQ3MTg4MzQ5NjYsImlzcyI6InVjIiwiZXhwIjoxNTk4MjU0NDc1LCJjdG0iOjE1OTU2NjI0NzYxMzgsImNpZCI6Ikp0WGJhTW43ZVAifQ.NgldzGp9fthLnKbyz3AfMP1SZhVL_nn-du6JMKilrSW4ujR6zSEh3-X0_j6Pmi3MDvw3uvLZZkF-RsD4HXHAhCAY2w5WQuDZICqWPO-mT_cFvMNchS_9TJHooOSNGtptmV2ip6DW45V0MH74Y0Z_HVMqfMr__NTr-EBZmjEcNzowJa9jexjisr7U64QmZ3ywzy_NJjlwbED_I1lXq3y0uCe7Ph684PIhnFkPymFFTuWg1iqcrKIM4YX61kstkBBilQ6OWzsmkO2Y-8WcQj5CsRZit5yhyGWy2ShbcvxW6IGDy6JAKMoZDthPhC0UfQhwK1WjVy2MD8OmgZ0C2ivdBA;u=4718834966;session_id=bf5e7516d10d16e5c076ef3e910ea8d2052407a089f29c414fb23363c644b174;xid=100306103',
    #         'User-Agent: Xueqiu Android 12.16',
    #         'Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    #         'X-Device-Model-Name: HUAWEI_BKL-AL20',
    #         'X-Device-OS: Android 10',
    #         'Host: xueqiu.yun.pingan.com'
    #     }
    #     url_list = "https://xueqiu.yun.pingan.com/tc/snowx/PAMID/newshare/list.json?_t=1HUAWEIb05075c0f9e1d7f678f3b46c1792bbd8.4718834966.1596179225241.1596179244992&_s=a46a4d&read_access_token=-6816049545399589140&x=0.213&aid=PAMID.69ecdce146a75c4702d6a6bcb44546c8c60495a842c58dd8cc5406c09700503b&tid=PAMID"
    #     result = requests.request('get', url_list, headers=header_list).json()
    #
    #     # 3 apply for the bond
    #
    #     # 4 notify


if __name__ == '__main__':
    unittest.main()
