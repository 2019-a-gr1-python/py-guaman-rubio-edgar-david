url = response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
contenedor = response.css('.product-tile-inner')
titulo = contenedor.css('a.name::text')
response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src').extract()
class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field()
primer_producto = ProductoFybeca()
primer_producto['titulo'] = titulo.extract_first()
primer_producto['imagen'] = url.extract_first()
primer_producto
def transformar_url_imagen(texto):
    url = 'https://fybeca.com'
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)
from scrapy.loader.processors import MapCompose
class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen))
    titulo = scrapy.Field()
primer_producto = ProductoFybeca()
primer_producto['titulo'] = titulo.extract_first()
primer_producto['imagen'] = url.extract_first()
primer_producto
class ProductoFybecaDos(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen))
    titulo = scrapy.Field()
primer_producto['imagen'] = url.extract_first()
primer_producto['titulo'] = titulo.extract_first()
from scrapy.loader import ItemLoader
il = ItemLoader(item=ProductoFybecaDos())
il.add_value('imagen',url.extract_first())
il.add_value('titulo',titulo.extract_first())
il.load_item()
%history -f ScrapyCSV.py
