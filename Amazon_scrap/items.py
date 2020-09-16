import scrapy

class AmazontutorialItem(scrapy.Item):
    product_name = scrapy.Field()
    Category_name = scrapy.Field()
    product_desc = scrapy.Field()
    product_price = scrapy.Field()
    product_imagelink = scrapy.Field()
    pass
