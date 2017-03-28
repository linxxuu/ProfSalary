import scrapy
import jsonpickle
import re
import os
from ..data import *

class GoogleScholarSpider(scrapy.Spider):
    name = "googlescholar"

    #input
    datapath = os.path.abspath(__file__ + "/../../../../../data")
    rooturl = "https://scholar.google.ch/"
    searchurl = "https://scholar.google.ch/citations?mauthors={0}&hl=en&view_op=search_authors"
    urls = []

    def __init__(self):
        with open(os.path.join(self.datapath, "income_results.json"), "rb") as file:
            for income in jsonpickle.decode(file.read()):
                fullname = income.lastname + " " + income.firstname
                url = self.searchurl.format(fullname)
                self.urls.append(url)

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for entity in response.css('.gs_scl').extract():
            if "Texas A&amp;M University" in entity:
                match = re.search(r'href=[\'"]?([^\'" >]+)', entity)
                if match:
                    detailpage = self.rooturl + match.group(0)[6:] + "&view_op=list_works&sortby=pubdate&cstart=0&pagesize=100"
                    print ">> parsing {0}".format(detailpage)
                    yield scrapy.Request(detailpage, callback=self.parse_detail)
    
    def parse_detail(self, response):
        
        # scholar
        scholar = response.css('#gsc_prf_in::text').extract_first()
        print "scholar: {0}".format(scholar)

        # statistics
        citations = response.css('tr:nth-child(2) .gsc_rsb_sc1+ .gsc_rsb_std::text').extract_first()
        hindex = response.css('tr:nth-child(3) .gsc_rsb_sc1+ .gsc_rsb_std::text').extract_first()
        i10index = response.css('tr:nth-child(4) .gsc_rsb_sc1+ .gsc_rsb_std::text').extract_first()

        # publications
        page_range = response.css('#gsc_a_nn::text').extract_first().split(u'\u2013')
        print page_range
        publications = []
        for page in range(int(page_range[0]), int(page_range[1]), 1):
            title = response.css('.gsc_a_tr:nth-child({0}) .gsc_a_at::text'.format(page)).extract_first()
            authors = response.css('.gsc_a_tr:nth-child({0}) .gsc_a_t .gs_gray::text'.format(page)).extract_first() 
            try:
                publisher = response.css('.gsc_a_tr:nth-child({0}) .gs_gray+ .gs_gray::text'.format(page)).extract_first()
            except expression as identifier:
                publisher = None
            citations = response.css('.gsc_a_tr:nth-child({0}) .gsc_a_ac::text'.format(page)).extract_first()
            year = response.css('.gsc_a_tr:nth-child({0}) .gsc_a_h::text'.format(page)).extract_first()
            publications.append(GoogleScholarPublication(
                title,
                authors,
                publisher,
                0 if citations==u'\u00a0' else int(citations), 
                year))
        
        # add to results
        yield {"data": GoogleScholarScholar(
            scholar,
            citations,
            hindex,
            i10index,
            publications
        )}