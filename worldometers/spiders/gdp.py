# -*- coding: utf-8 -*-
import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = [
        'www.worldpopulationreview.com/']
    start_urls = [
        'https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        pass
