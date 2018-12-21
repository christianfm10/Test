# -*- coding: utf-8 -*-
import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = (
        'http://quotes.toscrape.com/',
    )


    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tag = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        yield {"H1 Tag": h1_tag,"Tag": tag}
        # sneakers_prices = response.xpath('//*[@class="salesprice"]/text()').extract()   
        # sneakers_names = response.xpath('//*[@class="title"]/text()').extract()
        # sneakers_images = response.xpath('//*[@class="show lazyload"]/@data-original').extract()

        # sneakers_stars = response.xpath('//*[@class="rating-stars-count"]/text()').extract()
        # sneakers_stars = response.xpath('//*[@class="rating-stars rating-stars-filled"]/@style').extract()
        # sneakers_stars = response.xpath('//*[@class="rating-stars"]/text()')
        # print sneakers_stars
        # print ('Hola como estas')
        # for x in sneakers_prices:
        #     print(x)
        # for x in sneakers_names:
        #     print(x)
        # for x in sneakers_images:
        #     print(x)
