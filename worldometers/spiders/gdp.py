# -*- coding: utf-8 -*-
import scrapy


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = [
        'www.worldpopulationreview.com/']
    start_urls = [
        'https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        title = response.xpath("//td/h1/text()").get()
        countries_1 = response.xpath("//td/a/text()").getall()
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

        yield {
            'title': title,
            'countries_1': countries_1,
            'country_name': name,
            'country_link': link
        }
