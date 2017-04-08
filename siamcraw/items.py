#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class LoginItem(scrapy.Item):
    ccpassword = scrapy.Field()
    cdescribe = scrapy.Field()
    cidgrupo = scrapy.Field()
    cidusuario = scrapy.Field()
    csuspendido = scrapy.Field()
    userid = scrapy.Field()

class Link(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

class New(scrapy.Item):
    tema = scrapy.Field(
        output_processor=Join(),
    )
    titulo = scrapy.Field(
    	input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    texto = scrapy.Field(
    	input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    fecha = scrapy.Field(
        #input_processor=MapCompose(parse_date),
        output_processor=Join(),
    )
    keywords = scrapy.Field()