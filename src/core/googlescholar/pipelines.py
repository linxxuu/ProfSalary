# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import jsonpickle
import json

class GooglescholarPipeline(object):

    def __init__(self):
        print "test"

    def open_spider(self,spider):
        self.datapath = os.path.abspath(__file__ + "/../../../../data/googlescholar_results.dat")
        print ">>>>>>>>>>{0}".format(self.datapath)
        self.file = open(self.datapath, 'w+')

    def close_spider(self,spider):
        self.file = close
        
    def process_item(self, item, spider):
        line = json.dumps(dict(item))+"\n"
        self.file.write(line)
        return item
