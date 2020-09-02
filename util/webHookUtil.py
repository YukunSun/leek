# -*- coding: utf-8 -*-


"""
发送 markdown
"""
import json

import requests


def notify_by_qywechat(web_hook, body):
    robot_body = {
        "msgtype": "markdown",
        "markdown": {
            "content": body
        }
    }
    robot_result = requests.post(web_hook, data=json.dumps(robot_body),
                                 headers={"Content-Type": "application/json"}).json()
    return robot_result
