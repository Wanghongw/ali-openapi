# Ali-OpenApi

## 简介

依托于阿里巴巴相关服务，搭建起的服务平台。给大家提供更易用、简单的Api。

**该项目不依赖于任何框架，可独立运行。**

## 环境 

python3 以上

## 简单使用

### 初始化配置

目前 `tests` 目录下 `config.json` 有测试配置。

```

>>> from aliopenapi.api import AliApi
>>> ali_api = AliApi()
>>> ali_api.config.from_json("JSON_FILE_CONFIG_PATH")
True

```

### 生成支付链接

```python 

# pc 支付
>>> ali_api.pay.page.direct("双黄连口服液", "1231313123", "100")
`这里会出现支付链接，点击会跳转至支付宝支付页面`

# 移动端 支付
>>> ali_api.pay.wap.direct("双黄连口服液", "1231313123", "100")
`这里会出现支付链接，点击会跳转至支付宝支付页面`

# app 支付
>>> ali_api.pay.app.direct("双黄连口服液", "1231313123", "100")
`这里会出现支付链接，点击会拉起支付宝app进行支付`

```

## Ending

```
持续更新中，文档、更多的 api 支持
```

## Donate

如果本仓库对你有帮助，可以请作者喝杯白开水。  

Thanks ~ 

<img src="//hcdn2.luffycity.com/media/frontend/books/1711584789344_.pic.jpg" width = "216" />

## Support 

```
2020 By Liuzhichao.
```
