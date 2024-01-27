from scrapy.item import Item, Field


class Country(Item):
    name = Field(max_length=64, unique=True, primary_key=True, null=True)
    flage = Field(max_length=256)
    currency = Field(max_length=32) 
    code = Field(max_length=32)
    symbol = Field(max_length=32)

    