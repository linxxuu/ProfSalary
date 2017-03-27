import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from core.income.data import *
from core.income.parser import *
from core.googlescholar.spiders.gsspider import *

# Step 1
print "\n>> Step 1: fetch and parse income data "
incomeparser = IncomeParser()
incomeparser.run()

# Step 2
print "\n>> Step 2: scrap google scholar data "
settings = get_project_settings()
gssprocess = CrawlerProcess(settings)
gssprocess.crawl(GoogleScholarSpider)
gssprocess.start() # the script will block here until the crawling is finished