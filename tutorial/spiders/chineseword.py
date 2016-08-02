import scrapy

class wordscrapy(scrapy.Spider):
    name="word"
    allowed_domains=["xh.5156edu.com"]
    start_urls=["http://xh.5156edu.com/pinyi.html"]
