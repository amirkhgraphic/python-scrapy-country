import scrapy


class CountrySpider(scrapy.Spider):
    name = "country"
    start_urls = ["https://www.currencyremitapp.com/world-currency-symbols"]

    custom_settings = {
		'FEEDS': { 
            'data.json': { 
                'format': 'json',
                'overwrite': True,
            },
            'data.csv': {
                'format': 'csv',
                'overwrite': True
            }
        }
    }
    def parse(self, response):
        countries = response.css("tbody tr")

        for country in countries:
            name, currency, code, symbol = country.css("td::text").getall()
            flage = country.css("td img").attrib["src"]
            yield {
                    "name": name, 
                    "flage": flage, 
                    "currency": currency, 
                    "code": code, 
                    "symbol": symbol
                   }