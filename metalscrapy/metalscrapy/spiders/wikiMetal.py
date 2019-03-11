# -*- coding: utf-8 -*-
import scrapy
import re
import pandas as pd
import datetime

class WikimetalSpider(scrapy.Spider):
    name = 'wikiMetal'
    allowed_domains = ['metalstorm.net']
    start_urls = ['http://www.metalstorm.net/events/new_releases.php?upcoming=115085']

    def parse(self, response):
        artistaRE = re.compile =('(\-.\w.*)')
        albumRE = re.compile =('.*(\s-\s)')
        print("Procesando Lista de Albums...")

        try:
            fecha = response.xpath("//table[@class = 'table table-compact table-striped']/tr/td[@class='dark']/text()").extract()
            artistaAlbum = response.xpath("//table[@class = 'table table-compact table-striped']/tr/td/a/text()").extract()
                
            artistaL = [re.sub(artistaRE,'',str(artista)) for artista in artistaAlbum]
            albumL = [re.sub(albumRE,'',str(album)) for album in artistaAlbum]
            fechaL = [str(f)[0:2] + '/' + str(f)[3:5] + '/' + '2019' for f in fecha]

            lista = dict(ReleaseDate = fechaL, 
                         Band = artistaL, 
                         Album = albumL, 
                         LoadDate = "{:%d/%m/%Y}".format(datetime.date.today()))
            listaDF = pd.DataFrame(lista)
            listaDF.to_csv('albums.csv')
            
            print("Se proceso con exito la Lista de Albums :)")
        
        except:
            print('Fallo el procesamiento de la Lista de Albums :(')