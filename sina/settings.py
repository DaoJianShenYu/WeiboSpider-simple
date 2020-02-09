# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=272468376.380873; _T_WM=14861643098; SCF=AlvwCT3ltiVc36wsKpuvTV8uWF4V1tZ17ms9t-bZCAuisqitAF1puKEglaMyZOwEtSE0OSi5TP7KSKiUG8UbMfc.; SUB=_2A25x1IKODeRhGeVO7lUY8SrPzjiIHXVTNi7GrDV6PUJbktANLULmkW1NTX0wG4m2RAv9xPy53JZrwPqQsIXrjYZc; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhBzGKCgY_5TUiJzOmnqXu95JpX5KzhUgL.Foe7SKM4eKB0SKB2dJLoI0MLxKqL1-eLBKnLxKBLBo.LBK5LxKBLBo.LBK5LxK-LBKBLBK.LxK-LBKBLBK.LxKqL1K.LBoB_; SUHB=0xnS3iZrVsBuJ9; SSOLoginState=1557197534; MLOGIN=1; _T_WL=1; _WEIBO_UID=3057914354; M_WEIBOCN_PARAMS=luicode%3D20000174; WEIBOCN_FROM=1110106030'
}

# 当前是单账号，所以下面的 CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 请不要修改

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'
