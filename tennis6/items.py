# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Tennis6Item(Item):
    
    title = Field()
    imgurl = Field()
    nexturl = Field()
    des = Field()
    city=Field()
    district=Field()
    address=Field()
    phone=Field()
    courtNumber=Field()
    priceStart=Field()
    priceEnd=Field()
    level=Field()
    pass
