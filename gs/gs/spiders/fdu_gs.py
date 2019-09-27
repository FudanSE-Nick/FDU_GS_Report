# -*- coding: utf-8 -*-
import scrapy
from gs.items import GsItem

class FduGsSpider(scrapy.Spider):
    name = 'fdu_gs'
    allowed_domains = ['gs.fudan.edu.cn']
    start_urls = ['http://www.gs.fudan.edu.cn/tzgg/list1.htm']

    def parse(self, response):
        gs_list=response.xpath("//ul[@class='wp_article_list']/li")
        #print(gs_list)
        for i in gs_list:
            gs_item=GsItem()
            gs_item['title']=i.xpath(".//a/text()").extract_first()
            gs_item['datetime']=i.xpath("//span[@class='Article_PublishDate']/text()").extract_first()
            yield gs_item
        for i_req in range(14,1,-1):
            yield scrapy.Request("http://www.gs.fudan.edu.cn/tzgg/list"+str(i_req)+".htm",callback=self.parse)

