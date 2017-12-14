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


class Mombaby(CrawlSpider):
    name = "Mombaby"
    allowed_domains = ["mombaby.tw"]

    start_urls = ["https://mombaby.tw/articlecategory/children-education"]

    rules = (
        Rule(LinkExtractor(allow=('https://mombaby.tw/\d+\.html',)), callback="parse"),
    )

    def parse(self, response):
        item = Homework3Item()
        sel = Selector(response)
        sites = sel.xpath("//header[contains(@class,'entry-header')]")
        i = 0
        for site in sites:
            item["title"] = site.xpath(
                "//h2[contains(@class,'entry-title')]/a/text()").extract()[i]
            item["url"] = site.xpath(
                "//h2[contains(@class,'entry-title')]/a/@href").extract()[i]
            item["time"] = site.xpath(
                "//time[contains(@class,'entry-time')]/text()").extract()[i]
            i = i + 1
            yield item
        next_page = response.xpath(
            ".//li[contains(@class,'pagination-next')]/a/@href").extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = next_href
            request = scrapy.Request(url=next_page_url)
            yield request
