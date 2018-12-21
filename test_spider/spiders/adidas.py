# -*- coding: utf-8 -*-
import scrapy
import re

class AdidasSpider(scrapy.Spider):
    adidas_products = ["calzado-hombre","ropa-hombre","accesorios-hombre","performance-hombre"
    ,"calzado-mujer","ropa-mujer","accesorios-mujer","performance-mujer"
    ,"ninos?prefn1=age&prefv1=8-16%20A%C3%B1os&srule=newest-to-oldest"
    ,"ninos?prefn1=age&prefv1=4-8%20A%C3%B1os"
    ,"bebe-ninos"
    ,"performance-ninos"]
    name = 'adidas'
    allowed_domains = ['adidas.pe']
    start_urls = ['https://adidas.pe/{}'.format(i) for i in adidas_products]

    def parse(self, response):
        sneakers = response.xpath('//div[@class="hockeycard originals " or @class="hockeycard performance "]')
        print(len(sneakers))
        for sneaker in sneakers:
            sneaker_name = sneaker.xpath('.//*[@class="title"]/text()').extract()
            sneaker_price = re.findall(r'\d+', sneaker.xpath('.//*[contains(@class, "salesprice")]/text()').extract_first())[0]   
            sneaker_image = sneaker.xpath('.//*[@class="show lazyload"]/@data-original').extract_first()
            sneaker_url = sneaker.xpath('.//*[@class="image plp-image-bg"]/a/@href').extract_first()
            sneaker_star = sneaker.xpath('.//*[@class="rating-stars rating-stars-filled"]/@style').extract_first()
            # sneaker_star = int(re.findall(r'\d+',sneaker.xpath('.//*[@class="rating-stars rating-stars-filled"]/@style').extract_first())[0])    
            yield{  'Name' : sneaker_name,
                    'Prices' : sneaker_price,
                    'Image' : sneaker_image,
                    'URL' : sneaker_url,
                    'Stars' : sneaker_star
                  }
        next_page_url = response.xpath('//*[@class="paging-arrow pagging-next-page"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
