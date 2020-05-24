import scrapy
from ..items import ProjectNameItem
class quotesSpider(scrapy.Spider):
	name='quotes'
	start_urls=[
	'http://quotes.toscrape.com/page/1/'
	]
	page_number=2
	def parse(self,response):
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
		# next_page=response.css('li.next a::attr(href)').get()
		# if next_page is not None:
		# 	yield response.follow(next_page,callback=self.parse)
		next_page='http://quotes.toscrape.com/page/'+str(quotesSpider.page_number)+'/'
		if quotesSpider.page_number<11:
			quotesSpider.page_number+=1
			yield response.follow(next_page,callback=self.parse)