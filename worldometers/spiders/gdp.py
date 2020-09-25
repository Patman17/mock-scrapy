# -*- coding: utf-8 -*-
import scrapy
import logging


class GdpSpider(scrapy.Spider):
    name = 'gdp'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = [
        'https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            yield{
                'country_name': row.xpath('.//td[1]/a/text()').get(),
                'gdp_debt': row.xpath('.//td[2]/text()').get(),
                'population': row.xpath('.//td[3]/text()').get(),
            }

    # def parse(self, response):
    #     # title = response.xpath("//td/h1/text()").get()
    #     # countries_1 = response.xpath("//td/a/text()").getall()
        # countries = response.xpath("//td/a")
    #     name_list = []
    #     link_list = []
    #     for country in countries:
    #         name = country.xpath(".//text()").get()
    #         link = country.xpath(".//@href").get()
    #         name_list.append(name)
    #         link_list.append(link)

    #     GDP = response.xpath("//tr/td[2]/text()").getall()
    #     population = response.xpath("//tr/td[3]/text()").getall()

    #     yield {
    #         'country_name': name_list,
    #         'country_link': link_list,
    #         'GDP': GDP,
    #         'Population': population
    #     }

        # """1) Manual yielding just the items"""
        # # yield {
        # #     'title': title,
        # #     'countries_1': countries_1,
        # #     'country_name': name,
        # #     'country_link': link
        # # }

    #     """2) Utilize response to access the links"""
    #     # absolute_url = f'https://worldpopulationreview.com{link}'  ### 1) First method to getting URL
    #     # absolute_url = response.urljoin(link)  # 2) 2nd Method utilizing helper function to join URL
    #     # yield scrapy.Request(url=absolute_url)
    #     # 3) 3rd method
    #     yield response.follow(url=link, callback=self.parse_country)

    # def parse_country(self, response):
    #     logging.info(response.url)
