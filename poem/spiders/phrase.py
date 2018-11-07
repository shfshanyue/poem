# encoding: utf-8
import scrapy
import re

class PhraseSpider(scrapy.Spider):
    name = 'phrase'
    start_urls = [
        'https://so.gushiwen.org/mingju/default.aspx?p=1&c=&t='         
    ]

    def parse(self, response):
        for cont in response.xpath('/html/body/div[2]/div[1]/div[2]').css('.cont'):
            phrase, info = cont.css('a::text').extract()
            author = re.match(u'^[\u4e00-\u9fa5]+', info.strip()).group(0)
            title = re.search('<(.*?)>', info.replace('《', '<').replace('》', '>')).group(1)
            yield {
                'phrase': phrase,
                'author': author,
                'title': title,
            }
