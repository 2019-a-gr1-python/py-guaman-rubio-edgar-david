import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'arania_libros' #Heredado (conservar el nombre)

    allowed_domains = ['toscrape.com'] #Heredado (conservar el nombre)

    # start_urls es Heradado (conservar el nombre)
    start_urls = ['http://books.toscrape.com/']
    
    url_segmento_permitido = ('category/books/mystery_3','category/books/fantasy_19')
    
    regla_dos = (Rule(LinkExtractor(allow_domains=allowed_domains,allow=(url_segmento_permitido)),callback='parse_page'),)

    rules = regla_dos

    def parse_page(self, response):
        lista_programas = response.css('.product_pod > h3 > a::attr(title)').extract()

        for agencia in lista_programas:
            with open('libros_fantasia_misterio.txt','a+') as archivo:
                archivo.write(agencia + '\n')