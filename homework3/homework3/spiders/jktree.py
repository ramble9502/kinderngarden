# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
import sys
sys.path.append('..')

from items import Homework3Item


class Jktree(CrawlSpider):
    name = "Jktree"
    allowed_domains = ["jktree.com"]

    start_urls = ["http://www.jktree.com/baby/schoolage/"]

    rules = (
        Rule(LinkExtractor(allow=('/baby/schoolage/\d+\.html',)), callback="parse"),
    )

    def parse(self, response):
        item = Homework3Item()
        sel = Selector(response)
        sites = sel.xpath("//div[contains(@class,'m-article-box__item')]")
        i = 0
        for site in sites:
            item["title"] = site.xpath(
                "//a[contains(@class,'lamp')]/text()").extract()[i]
            item["url"] = "http://www.jktree.com"+site.xpath(
                "//a[contains(@class,'lamp')]/@href").extract()[i]
            a = site.xpath(
                "//div[contains(@class,'_info hide-for-small-only')]/span/text()").extract()[i]
            aextra = datetime.strptime(a, '%b %d, %Y').strftime('%Y-%m-%d')
            item["time"] = aextra
            i = i + 1
            yield item
        next_page = response.xpath('.//a[@rel="next"]/@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http://www.jktree.com' + next_href
            request = scrapy.Request(url=next_page_url)
            yield request
