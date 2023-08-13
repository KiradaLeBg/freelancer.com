# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FreelancerPipeline:
    def process_item(self, item, spider):
        return item

import psycopg2

class PostgresPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='ieeeeee.',
            dbname='JobListings'
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO JobListings (job_title, description, location, price, proposal, link)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (item['job_title'], item['description'], item['location'], item['price'], item['proposal'], item['link']))
        self.connection.commit()
        return item
