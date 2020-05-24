import scrapy
from ..items import ProjectNameItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
class quotesSpider(scrapy.Spider):
	name='quotes'
	start_urls=[
	'http://quotes.toscrape.com/login',
	]
	def parse(self,response):
		token=response.css('form input::attr(value)').extract_first()
		print(token)
		return FormRequest.from_response(response,formdata={'csrf_token':token,
															'username':'piyush',
															'password':'123'},
															callback=self.start_scraping)
	def start_scraping(self,response):
		open_in_browser(response)
		items=ProjectNameItem()
		all_div_quotes=response.css("div.quote")
		for quotes in all_div_quotes:
			title=quotes.css('span.text::text').extract()
			author=quotes.css('.author::text').extract()
			tag=quotes.css('.tag::text').extract()
			# yield{
			# 'title':title,
			# 'author':author,
			# 'tag':tag
			# }
			items['title']=title
			items['author']=author
			items['tag']=tag
			yield items
		next_page=response.css('li.next a::attr(href)').get()
		if next_page is not None:
			yield response.follow(next_page,callback=self.start_scraping)