#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy


class WebsiteInforGetSpider(scrapy.Spider):

    # 初始化，提取爬虫名字，start_ruls
    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        # 如果爬虫没有名字，中断后续操作则报错
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)

        # URL列表。当没有指定的URL时，spider将从该列表中开始进行爬取。
        # 因此，第一个被获取到的页面的URL将是该列表之一。
        # 后续的URL将会从获取到的数据中提取。
        if not hasattr(self, 'start_urls'):
            # 这个地方去取数据库中的企业网址；   或者从外部控制程序传入
            self.start_urls = []

    # 或者重写这个方法
    def start_requests(self):
        # 先找出满足匹配条件的链接
             ......

        if 链接文本满足企业简介的的匹配：
            yield scrapy.Request('https://www.glprop.com.cn/press-releases.html', self.parse1)
        if 链接文本满足联系方式的匹配：
            yield scrapy.Request('https://www.glprop.com.cn/in-the-news.html', self.parse2)
        if 链接文本足荣誉资质的匹配
            yield scrapy.Request('https://www.glprop.com.cn/proposed-privatization.html', self.parse3)


    # 企业网址首页分析程序
    def parse(self, response):
        #爬取首页上满足匹配的条件的链接
          .....
        # 对爬到的链接进行分别处理
        if  xxx:  # 如果是满足企业介绍的链接
           ...
          yield scrapy.Request(url, callback=self.parse_introduce)

        if  xxx:  # 如果是满足企业联系方式的链接
           ...
          yield scrapy.Request(url, callback=self.parse_contact)

    def parse_introduce(self, response):
        .....
        yield introduce_item

    def parse_contact(self, response):
        .....
        yield contact_item