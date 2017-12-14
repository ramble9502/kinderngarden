# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import sys
from scrapy import log
from sqlite3 import dbapi2 as sqlite
import sqlite3 as lite
# Define your item pipelines here
#
from twisted.enterprise import adbapi

con = None


class Homework3Pipeline(object):

    def __init__(self):
        self.setupDBCon()

    def process_item(self, item, spider):
        if spider.name == 'Jktree':
            self.storeInDb(item)
            return item
        if spider.name == 'Mmready':
            self.storeInMmreadyDb(item)
            return item
        if spider.name == 'Mombaby':
            self.storeInMomDb(item)
            return item
        return item

    def storeInDb(self, item):
        self.cur.execute(
            "INSERT INTO one_jktree (title,url,time) values(?,?,?)", (item["title"], item["url"], item["time"]))
        self.con.commit()

    def storeInMmreadyDb(self, item):
        self.cur.execute(
            "INSERT INTO one_mmready (title,url,time) values(?,?,?)", (item["title"], item["url"], item["time"]))
        self.con.commit()

    def storeInMomDb(self, item):
        self.cur.execute("INSERT INTO one_mombaby(title,url,time) values(?,?,?)", (item[
                         "title"], item["url"], item["time"]))
        self.con.commit()

    def setupDBCon(self):
        self.con = lite.connect(
            "C:\kinderngarden\db.sqlite3")
        self.cur = self.con.cursor()


class OnePipeline(object):

    def __init__(self):
        self.file = codecs.open('items.json', mode='a',  encoding="utf-8")

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.encode().decode())
        return item

    def spider_closed(self, spider):
        self.file.close()


class TwoPipeline(object):

    def __init__(self):
        self.file = codecs.open('items.json', mode='w',  encoding="utf-8")
        pass

