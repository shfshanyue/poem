# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from model import Phrase, db_connect, create_deals_table
from sqlalchemy.orm import sessionmaker

class PoemPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        phrase = Phrase(**item)

        try:
            session.add(phrase)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
