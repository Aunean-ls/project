# -*- coding: utf-8 -*-

# Scrapy settings for dianpingPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dianpingPro'

SPIDER_MODULES = ['dianpingPro.spiders']
NEWSPIDER_MODULE = 'dianpingPro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Cookie': 'lgtoken=04d5b4b63-f50f-4701-873f-cb686fdea05e; thirdtoken=542f53b3-3259-405c-bc2a-29a6fe9024e7; dplet=45dcd95b2c7e1cc2c028bb808f1f3b6b; dper=9e2ec7f7ae0a361117e405578541cedcde5146b0e18890060195789c601e0564199e6e85e1d1d060388dae0bebea14b3afb49b4dd355678ffd467dbff8fd9219; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_8517583926; ctu=3877de628f129d466680c64a83ca271add57718a0310c1a76b4f2150a544e11d; fspop=test; cy=344; cye=changsha; _lxsdk_cuid=17655e01e9ba-0f3973c7e1d8fa-4c3f2779-144000-17655e01e9cc8; _lxsdk_s=17655e01e9d-6d4-5ac-1d0%7C%7C57; _lxsdk=17655e01e9ba-0f3973c7e1d8fa-4c3f2779-144000-17655e01e9cc8; _hc.v=dcba044f-796d-7250-b9c7-2c1ac14c469c.1607758521; JSESSIONID=D243D2DCCA22BE56996069C93C83A70D'
#
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dianpingPro.middlewares.DianpingproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dianpingPro.middlewares.DianpingproDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'dianpingPro.pipelines.DianpingproPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
