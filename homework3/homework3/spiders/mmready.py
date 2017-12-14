# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import CrawlSpider, Rule
import sys
sys.path.append('..')

from items import Homework3Item


class Mmready(CrawlSpider):
    name = "Mmready"
    allowed_domains = ["mmready.com"]

    start_urls = ["http://www.mmready.com/育兒_1.html"]

    rules = [
        Rule(LinkExtractor(allow=r'//www.mmready.com/育兒_[0-9].html'),
             callback='parse', follow=True)
    ]

    def parse(self, response):
        item = Homework3Item()
        sel = Selector(response)
        sites = sel.xpath("//li[contains(@class,'item img0')]")
        i = 0
        for site in sites:
            item["title"] = site.xpath(
                "//h3/a/text()").extract()[i]
            item["url"] = "http:"+site.xpath(
                "//h3/a/@href").extract()[i]
            item['time'] = site.xpath(
                "//div[contains(@class,'cdata')]/span/a/text()").extract()[i]
            i = i + 1
            yield item
        next_page = response.xpath(
            ".//a[contains(@class,'cur')]/following-sibling::node()/@href").extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http:' + next_href
            request = scrapy.Request(url=next_page_url)
            yield request
