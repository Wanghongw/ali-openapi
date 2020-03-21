#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/8/2

"""
    实名认证相关接口实现, 实名认证三步走

        认证初始化 > 开始认证 > 认证查询
"""


from .base import BaseAliClientAPI


class AliCertify(BaseAliClientAPI):

    def initialize(self, outer_order_no, biz_code, identity_param, merchant_config, **kwargs):
        """身份认证初始化服务

        文档DOC地址: https://docs.open.alipay.com/api_2/alipay.user.certify.open.initialize/

        Parameters
        ----------
        outer_order_no: string
            商户请求的唯一标识

        biz_code: string
            认证场景码。入参支持的认证场景码和商户签约的认证场景相关，取值如下:
            FACE：多因子人脸认证
            CERT_PHOTO：多因子证照认证
            CERT_PHOTO_FACE ：多因子证照和人脸认证
            SMART_FACE：多因子快捷认证

        identity_param: json
            需要验证的身份信息参数，格式为json，字段详细说明如下：
            identity_type：身份信息参数类型，必填，必须传入CERT_INFO
            cert_type：证件类型，必填，当前支持身份证，必须传入IDENTITY_CARD
            cert_name：真实姓名，必填，填写需要验证的真实姓名
            cert_no：证件号码，必填，填写需要验证的证件号码

        merchant_config: json
            商户个性化配置，格式为json，详细支持的字段说明为：
            return_url：需要回跳的目标地址，必填，一般指定为商户业务页面

        kwargs: dict
            face_contrast_picture: string
                自定义人脸比对图片的base64编码格式的string字符串

        Returns
        -------
        string
        """
        biz_content = {
            "outer_order_no": outer_order_no,
            "biz_code": biz_code,
            "identity_param": identity_param,
            "merchant_config": merchant_config
        }
        biz_content.update(**kwargs)
        return self._get(self._generate_url("alipay.user.certify.open.initialize", biz_content))

    def certify(self, certify_id):
        """开始认证流程

        文档DOC地址: https://docs.open.alipay.com/api_2/alipay.user.certify.open.certify/

        Parameters
        ----------
        certify_id: string
            本次申请操作的唯一标识，由开放认证初始化接口调用后生成，后续的操作都需要用到

        Returns
        ----------
        dict
        ----------
        For example:
            {
                "alipay_user_certify_open_certify_response": {
                    "code": "10000",
                    "msg": "Success"
                },
                "sign": "ERITJKEIJKJHKKKKKKKHJEREEEEEEEEEEE"
            }
        """
        biz_content = {
            "certify_id": certify_id,
        }

        return self._generate_url("alipay.user.certify.open.certify", biz_content)

    def query(self, certify_id):
        """身份认证记录查询

        文档DOC地址: https://docs.open.alipay.com/api_2/alipay.user.certify.open.query/

        Parameters
        ----------
        certify_id: string
            本次申请操作的唯一标识，由开放认证初始化接口调用后生成，后续的操作都需要用到

        Returns
        ----------
        dict
        ----------
        For example:
            {
                "alipay_user_certify_open_query_response": {
                    "code": "10000",
                    "msg": "Success",
                    "passed": [
                        "T"
                    ],
                    "identity_info": "{}",
                    "material_info": "{}"
                },
                "sign": "ERITJKEIJKJHKKKKKKKHJEREEEEEEEEEEE"
            }
        """
        biz_content = {
            "certify_id": certify_id,
        }
        url = self._generate_url("alipay.user.certify.open.query", biz_content)

        return self._get(url)
