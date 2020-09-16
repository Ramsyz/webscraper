import scrapy
from items import AmazontutorialItem
class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://giant.sg/dairy-chilled-frozen']


    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.product-link').css('::text').extract()
        Category_name = response.css('.to-brand-page').css('::text').extract()
        #product_price = response.css('.product-price').css(''::text').extract()
        product_desc = response.css('.size').css('::text').extract()
        product_price = response.css('.product-price').css('::text').extract()
        product_imagelink = response.css('.label::attr(src)').extract()

        items['product_name'] = product_name
        items['Category_name'] = Category_name
        items['product_desc'] = product_desc
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
