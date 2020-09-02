import os
import unittest

import requests

from util.webHookUtil import notify_by_qywechat


class MyTestCase(unittest.TestCase):
    # def setUp(self) -> None:
    #     pass
    #
    # def tearDown(self) -> None:
    #     pass

    def test_valuation(self):
        robot = os.getenv('WEB_HOOK_FUND')
        if robot == '':
            print("WEB_HOOK_FUND is empty")
        url = 'https://danjuanapp.com/djapi/fundx/activity/user/vip_valuation/show/detail?source=lsd'
        header = {
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "elastic-apm-traceparent": "00-b3eaa5c91267b277c2fc12f8f2d9ad5d-181e1450efc5178f-01",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://danjuanapp.com/screw/valuation-table?channel=1500012085",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cookie": "device_id=web_BkXA7l8kv; xq_a_token=d21e060f554a2b9e4493942a772d0bba812ff3f3; Hm_lvt_b53ede02df3afea0608038748f4c9f36=1594389456; _ga=GA1.2.1870501156.1594389458; gr_user_id=cc96a589-5fb0-4551-8a36-62a1e964692c; _gid=GA1.2.1354781524.1595165797; gr_session_id_94b96c7a661bf17a=0acfc23d-0345-4f87-aa30-8dcf884cfc67; gr_session_id_94b96c7a661bf17a_0acfc23d-0345-4f87-aa30-8dcf884cfc67=true; channel=1500012085; timestamp=1595168654221; Hm_lpvt_b53ede02df3afea0608038748f4c9f36=1595168654"
        }
        result = requests.request('get', url, headers=header).json()
        data = result['data']
        time = data['time']
        grade = data['grade']
        # "[{'id': 9741, 'relation_id': 4025, 'valuation_status': '1', 'index_name': '300价值', 'index_code': '000919', 'pe': 9.92, 'pb': 0.98, 'outside_fund': '519671', 'roe': 0.0993, 'dividend_yield': 0.0377, 'profit_yield': 0.1008}, {'id': 9742, 'relation_id': 4025, 'valuation_status': '1', 'index_name': '50AH优选', 'index_code': 'SH000170', 'pe': 9.94, 'pb': 1.07, 'inside_fund': '501050', 'outside_fund': '501050', 'roe': 0.1076, 'dividend_yield': 0.0325, 'profit_yield': 0.1006}, {'id': 9743, 'relation_id': 4025, 'valuation_status': '1', 'index_name': '上证红利', 'index_code': '000015', 'pe': 9.95, 'pb': 1.03, 'inside_fund': '510880', 'roe': 0.1039, 'dividend_yield': 0.0472, 'profit_yield': 0.1005}, {'id': 9744, 'relation_id': 4025, 'valuation_status': '1', 'index_name': '基本面50', 'index_code': 'SH000925', 'pe': 9.73, 'pb': 1.02, 'inside_fund': '160716', 'outside_fund': '160716', 'roe': 0.1047, 'dividend_yield': 0.0305, 'profit_yield': 0.1028}, {'id': 9745, 'relation_id': 4025, 'valuation_status': '1', 'index_name': 'H股指数', 'index_code': 'HKHSCEI', 'pe': 8.86, 'pb': 0.97, 'inside_fund': '510900', 'outside_fund': '110031', 'roe': 0.1098, 'dividend_yield': 0.0365, 'profit_yield': 0.1129}, {'id': 9746, 'relation_id': 4025, 'valuation_status': '1', 'index_name': '中证银行', 'index_code': 'SZ399986', 'pb': 0.9, 'inside_fund': '512800', 'outside_fund': '001594'}, {'id': 9747, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '中证红利', 'index_code': 'SH000922', 'pe': 10.18, 'pb': 1.05, 'outside_fund': '090010', 'roe': 0.1028, 'dividend_yield': 0.0447, 'profit_yield': 0.0982}, {'id': 9748, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '恒生指数', 'index_code': 'HKHSI', 'pe': 9.9, 'pb': 0.97, 'inside_fund': '159920', 'outside_fund': '000071', 'roe': 0.0977, 'dividend_yield': 0.0404, 'profit_yield': 0.101}, {'id': 9749, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '上证50', 'index_code': 'SH000016', 'pe': 10.4, 'pb': 1.18, 'inside_fund': '510710', 'outside_fund': '110003', 'roe': 0.1134, 'dividend_yield': 0.0259, 'profit_yield': 0.0962}, {'id': 9750, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '红利机会', 'index_code': 'CSPSADRP', 'pe': 14.17, 'pb': 1.6, 'inside_fund': '501029', 'outside_fund': '501029', 'roe': 0.1129, 'dividend_yield': 0.033}, {'id': 9751, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '沪深300', 'index_code': 'SH000300', 'pe': 12.78, 'pb': 1.43, 'inside_fund': '510310', 'outside_fund': '110020', 'roe': 0.112, 'dividend_yield': 0.0204}, {'id': 9752, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '央视50', 'index_code': 'SZ399550', 'pe': 10.76, 'pb': 1.27, 'inside_fund': '159965', 'outside_fund': '217027', 'roe': 0.1176, 'dividend_yield': 0.0277, 'profit_yield': 0.0929}, {'id': 9753, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '香港中小', 'index_code': 'SPHCMSHP', 'pe': 14.04, 'pb': 1.58, 'inside_fund': '501021', 'outside_fund': '501021', 'roe': 0.1125}, {'id': 9754, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '上证180', 'index_code': '000010', 'pe': 11.68, 'pb': 1.18, 'inside_fund': '510180', 'outside_fund': '040180', 'roe': 0.1008, 'dividend_yield': 0.0251, 'profit_yield': 0.0856}, {'id': 9755, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '500低波动', 'index_code': 'CSI930782', 'pe': 28.41, 'pb': 1.48, 'inside_fund': '512260', 'outside_fund': '003318', 'roe': 0.0521, 'dividend_yield': 0.0161}, {'id': 9756, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '基本面120', 'index_code': '399702', 'pe': 21.77, 'pb': 2.6, 'inside_fund': '159910', 'outside_fund': '070023', 'roe': 0.1192, 'dividend_yield': 0.0115}, {'id': 9757, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '中证500', 'index_code': 'SH000905', 'pe': 30.71, 'pb': 2.07, 'inside_fund': '510580', 'outside_fund': '161017', 'roe': 0.0675, 'dividend_yield': 0.0107}, {'id': 9758, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '可选消费', 'index_code': 'SH000989', 'pe': 34.48, 'pb': 2.39, 'inside_fund': '159936', 'outside_fund': '001133', 'roe': 0.0694, 'dividend_yield': 0.0155}, {'id': 9759, 'relation_id': 4025, 'valuation_status': '2', 'index_name': '证券行业', 'index_code': '399975', 'pb': 2.02, 'inside_fund': '512000', 'outside_fund': '004069'}, {'id': 9760, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '深证100', 'index_code': 'SZ399330', 'pe': 29.43, 'pb': 3.75, 'inside_fund': '159901', 'outside_fund': '161227', 'roe': 0.1275, 'dividend_yield': 0.0078}, {'id': 9761, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '深证成指', 'index_code': '399001', 'pe': 32.03, 'pb': 3.19, 'inside_fund': '159943', 'outside_fund': '163109', 'roe': 0.0997, 'dividend_yield': 0.0078}, {'id': 9762, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '基本面60', 'index_code': '399701', 'pe': 20.47, 'pb': 2.55, 'inside_fund': '159916', 'outside_fund': '530015', 'roe': 0.1244, 'dividend_yield': 0.0121}, {'id': 9763, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '中证消费', 'index_code': '000932', 'pe': 38.44, 'pb': 8.23, 'inside_fund': '159928', 'outside_fund': '000248', 'roe': 0.2141, 'dividend_yield': 0.008}, {'id': 9764, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '纳斯达克100', 'index_code': 'NDX', 'pe': 30.28, 'pb': 7.35, 'inside_fund': '513100', 'outside_fund': '160213', 'roe': 0.2428}, {'id': 9765, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '中证养老', 'index_code': 'SZ399812', 'pe': 29.93, 'pb': 3.72, 'outside_fund': '000968', 'roe': 0.1242, 'dividend_yield': 0.0097}, {'id': 9766, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '标普500', 'index_code': 'SP500', 'pe': 27.05, 'pb': 3.59, 'inside_fund': '513500', 'outside_fund': '050025', 'roe': 0.1328}, {'id': 9767, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '医药100', 'index_code': '000978', 'pe': 47.83, 'pb': 6.09, 'outside_fund': '001550', 'roe': 0.1273, 'dividend_yield': 0.0056}, {'id': 9768, 'relation_id': 4025, 'valuation_status': '3', 'index_name': '创业板指数', 'index_code': 'SZ399006', 'pe': 67.18, 'pb': 8, 'inside_fund': '159915', 'outside_fund': '161022', 'roe': 0.119, 'dividend_yield': 0.0027}]"
        valuations = data['valuations']
        template_title = "基金估值 <font color=\"warning\">{}</font> **评级**:{}(1星为泡沫阶段，5星为投资价值最高阶段)\n".format(time, grade)
        template_link = "[原文](https://danjuanapp.com/screw/valuation-table)"
        body = template_title + template_link
        robot_result = notify_by_qywechat(robot, body)
        self.assertEqual(robot_result['errcode'], 0)


if __name__ == '__main__':
    unittest.main()
