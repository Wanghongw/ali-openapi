#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/8/2

"""
    阿里 api 调用出口

        封装更易用的api
"""

from .pay.basic import AliPay
from .yun.basic import AliYunClient

from .config import Config


class AliApi(object):

    config_class = Config

    default_config = {
        "DEBUG": True,
        "CLOUD": {
            "APP_ID": None,
            "SECRET": None
        },
        "PAY": {
            "APP_ID": None,
            "PUBLIC_KEY_PATH": None,
            "PRIVATE_KEY_PATH": None,
            "NOTIFY_URL": None,
            "RETURN_URL": None
        }
    }

    def __init__(self, ):
        self.config = self.make_config()

    def make_config(self):
        defaults = dict(self.default_config)
        return self.config_class(defaults)

    @property
    def pay(self):

        pay_config = self.config["PAY"]
        app_id = pay_config["APP_ID"]
        public_key_path = pay_config["PUBLIC_KEY_PATH"]
        private_key_path = pay_config["PRIVATE_KEY_PATH"]
        notify_url = pay_config["NOTIFY_URL"]
        return_url = pay_config["RETURN_URL"]

        return AliPay(
            app_id=app_id, public_key_path=public_key_path,
            private_key_path=private_key_path, notify_url=notify_url,
            return_url=return_url, debug=self.config["DEBUG"]
        )

    @property
    def yun(self):

        cloud_config = self.config["CLOUD"]
        app_id = cloud_config["APP_ID"]
        secret = cloud_config["SECRET"]

        return AliYunClient(
            app_id=app_id, secret=secret
        )
