# -*- coding: utf-8 -*-
import scrapy


class PlazaveaSpider(scrapy.Spider):
    plazavea_products = ['electro/televisores/buscapagina?fq=C:/679/687/&PS=24&sl=3fae6b43-f32a-4e46-9aa1-44d37576301a&cc=12&sm=0&PageNumber={}'.format(i) for i in range(6)]
    computo = [ 'electro/computo/buscapagina?fq=C:/679/683/&PS=24&sl=3fae6b43-f32a-4e46-9aa1-44d37576301a&cc=12&sm=0&PageNumber={}'.format(i) for i in range(6)]
    plazavea_products = plazavea_products+computo
    name = 'plazavea'
    allowed_domains = ['tienda.plazavea.com.pe']
    start_urls = ['http://tienda.plazavea.com.pe/{}'.format(i) for i in plazavea_products]
#electro/televisores/tv-led/']
    # start_urls = ['https://tienda.plazavea.com.pe/buscapagina?fq=C%3a%2f679%2f687%2f776%2f&PS=24&sl=3fae6b43-f32a-4e46-9aa1-44d37576301a&cc=12&sm=0&PageNumber=2']
    # https://tienda.plazavea.com.pe/buscapagina?fq=C%3a%2f679%2f687%2f776%2f&PS=24&sl=3fae6b43-f32a-4e46-9aa1-44d37576301a&cc=12&sm=0&PageNumber=3

    def parse(self, response):
        # print(response.body)
        products = response.xpath('//*[@class="g-inner-prod"]')
        for product in products:
            normal_price = product.xpath('.//*[@class="g-block g-pnormal"]/span/text()').extract_first()
            # low_price = product.xpath('.//*[@itemprop="lowprice"]/text()').extract_first()
            low_price =  product.xpath('.//*[@class="g-block g-pmejor"]/p[@itemprop="lowprice"]/text()').extract_first()
            # priceOH = product.xpath('.//*[@itemprop="hightPrice"]/text()').extract_first()
            name = product.xpath('.//*[@class="g-nombre-complete"]/text()').extract_first()
            image = product.xpath('.//*[@class="g-img-prod"]/figure/img/@src').extract_first()
            url = product.xpath('.//*[@class="g-img-prod"]/@href').extract_first()
            yield {'name':name,
                    'normal_price':normal_price,
                    'low_price': low_price,
                    'image': image,
                    'url': url
                    }