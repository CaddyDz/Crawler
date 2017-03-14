from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class spider:
	
	# Class variables (shared among all instances)
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()
	
	def __init__(self, project_name, base_url, domain_name):
		spider.project_name = project_name
		spider.base_url = base_url
		spider.domain_name = domain_name
		spider.queue_file = spider.project_name + '/queue.txt'
		spider.crawled_file = spider.project_name + '/crawled.txt'
		self.boot()
		self.crawl_page('First spider', spider.base_url)

	@staticmethod
	def boot():
		createProjectDir(spider.project_name)
		createDataFiles(spider.project_name, spider.base_url)
		spider.queue = fileToSet(spider.queue_file)
		spider.crawled = fileToSet(spider.crawled_file)
	 
