# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://zsunion.taobao.com/?spm=a217m.8316598.1041398.14.3a9e33d5OrlNnJ/']

    def parse(self, response):
        self.log("image:%s" %response.xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/dl[1]/dt/a/text()').re('<a href=')
        self.log("title:%s" %response.xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/dl[1]/text()').extract())
        