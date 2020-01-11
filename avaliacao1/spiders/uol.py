# -*- coding: utf-8 -*-
import scrapy


class UolSpider(scrapy.Spider):
    name = 'uol'    
    start_urls = ['https://www.uol.com.br/']

    def parse(self, response):
        cotacaodolar = response.css('.HU_currency__quote.HU_currency__quote-up::text').extract_first()
        print('A cotação atual do dolar é: ', cotacaodolar)
