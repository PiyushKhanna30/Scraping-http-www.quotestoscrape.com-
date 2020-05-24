# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class ProjectNamePipeline(object):
	def __init__(self):
		self.create_connection()
		self.create_table()
	def create_connection(self):
		self.conn=psycopg2.connect(database="Scrapy",user="postgres",password="123",host="localhost")
		self.curr=self.conn.cursor()
	def create_table(self):
		self.curr.execute("""Drop table if exists quotes_table""")
		self.curr.execute("""create table quotes_table ( title text,author text,tag text) ;""")
	def store_db(self,item):
		self.curr.execute("""insert into quotes_table values (%s,%s,%s)""",	(item['title'][0],item['author'][0],item['tag'][0],))
		self.conn.commit()
	def process_item(self, item, spider):
		self.store_db(item)
		return item