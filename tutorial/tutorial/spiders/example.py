# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


def obtain_job_list(file):
    file = file.decode('utf-8')
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = tuple(lines)
        return lines


class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["sephora.cn"]
    job_list = r'C:\workspace\化妆品电商\job_List\job_list.txt'

    start_urls = obtain_job_list(job_list)

    def parse(self, response):
        base_xpath = "/html/body/div[@id='main']/div[@class='spriteLine clearFix']/div[@id='contentRight']/div[@id='globalFilterFacetProductDIV']/div[@id='rightCategoryFilterResultDiv']/div[@class='productList productBox cagegoryList mt20 mMt10 clearFix']"
        for sel in response.xpath(base_xpath + r'//div[@class="proBox"]'):
            item = TutorialItem()
            item['brand'] = sel.xpath('p[@class="proBrand"]/a/text()').extract()
            item['title'] = sel.xpath('div[@class="proTit"]/a/@title').extract()
            yield item
