# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    # allowed_domains = ['www.worldometers.info/world-population/population-by-country']
    allowed_domains = ['www.worldometers.info']
    start_urls = [
        'https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # Using manual way to set absolute url
            # absolute_url = f'https://www.worldometers.info{link}'

            # Helper method to get absolute url
            # absolute_url = response.urljoin(link)
            # use with absolute url above
            # yield scrapy.Request(url=absolute_url)

            yield response.follow(url=link)

            # pulling just country name and link
            # yield{
            #     'country_name': name,
            #     "country_link": link
            # }
