# -*- coding: utf-8 -*-
import scrapy


class GlassOffersSpider(scrapy.Spider):
    name = 'glass_offers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers/']

    # def start_request(self):
    #     yield scrapy.Request(url='https://https://www.glassesshop.com/bestsellers/', callback=self.parse, headers={
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    #     })

    def parse(self, response):
        glasses = response.xpath(
            "//div[@id='product-lists']/div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']")
        for glass in glasses:
            yield {
                'product_name': glass.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'product_url': glass.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'image_url': glass.xpath("//div[@class='product-img-outer']//img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'price': glass.xpath("//div[@class='p-price']//span/text()").get(),
            }

        next_page = response.xpath("//a[@class='page-link']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
            })
