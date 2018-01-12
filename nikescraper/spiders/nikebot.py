# -*- coding: utf-8 -*-
import scrapy


class NikebotSpider(scrapy.Spider):
    name = 'nikebot'
    allowed_domains = ['https://store.nike.com/in/en_gb/pw/mens-shoes/7puZoi3?ipp=120']
    start_urls = ['https://store.nike.com/in/en_gb/pw/mens-shoes/7puZoi3?ipp=120']

    def parse(self, response):
         product_name=response.css(".product-name .product-display-name ::text").extract()
         product_subtitle=response.css(".product-name .product-subtitle ::text").extract()
         product_price=response.css(".product-price .prices .local ::text").extract()
         product_no_colors=response.css(".product-group-details .number-of-colors ::text").extract()
         
         item={}
         for item in zip(product_name,product_subtitle,product_price,product_no_colors):
            scraped_info = {
            'product_name':item[0], 
            'product_subtitle': item[1],
            'product_price': item[2],
            'product_no_colors': item[3]
           }
         yield scraped_info
