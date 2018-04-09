import scrapy

class QidianSpider(scrapy.Spider):
    name = "qidian"
    main_url = 'http://www.23us.so/list/'
    end_url = '.html'

    def start_requests(self):
         for i in range(1,10):
             url = self.main_url + str(i) + '_1' +self.end_url
             yield scrapy.Request(url,self.parse)
         yield scrapy.Request('http://www.23us.so/full.html',self.parse)

    def parse(self, response):
        print(response.text)
