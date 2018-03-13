# -*- coding: utf-8 -*-
import scrapy
from ts.items import TsItem
from scrapy.http import Request

class LessonSpider(scrapy.Spider):
    name = '58'
    allowed_domains = ['58.com']
    start_urls = ['http://gz.58.com/ershoufang/pn1/']

    def parse(self, response):
        item=TsItem()
        item["title"]=response.xpath("//h2[@class='title']/a/text()").extract()
        item["money"]=response.xpath("//div[@class='price']/p[@class='sum']/b/text()").extract()
        #item["stu"]=response.xpath("//span[@class='course-view']/text()").extract()
        yield item
        for i in range(2,5):
            url="http://gz.58.com/ershoufang/pn"+str(i)
            yield Request(url,callback=self.parse)
