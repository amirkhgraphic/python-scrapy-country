# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class CountryPipeline:
    def open_spider(self, spider):
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()
        self.cur.execute('''DROP TABLE IF EXISTS country''')
        self.cur.execute('''CREATE TABLE country
                       (name text, flage text, currency text, code text, symbol text)''') # create a table
        self.con.commit()

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into country values (?, ?, ?, ?, ?)",
                         (item['name'], item['flage'], item['currency'], item['code'], item['symbol']))
        self.con.commit()
        return item
