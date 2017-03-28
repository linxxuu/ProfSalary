# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import jsonpickle
import json
import os

class GooglescholarPipeline(object):

    def __init__(self):
        self.datapath = os.path.abspath(__file__ + "/../../../../data/googlescholar_results.json")

    def open_spider(self,spider):
        self.scholars = []

    def close_spider(self,spider):
        with open(self.datapath, "w+") as file:
            file.write("{{\"scholars\": {0}}}".format(jsonpickle.encode(self.scholars)))
        
    def process_item(self, item, spider):
        print dict(item)
        self.scholars.append(item["data"])
        return item
