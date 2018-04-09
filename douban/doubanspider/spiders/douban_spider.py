from scrapy import Request
from scrapy import Selector
from scrapy import Spider
from doubanspider.items import DoubanItem


class DoubanSpider(Spider):
    name = 'doubanspider'
    allowed_domains = ["movie.douban.com"]
    start_urls = ['http://movie.doubanspider.com/top250']

    def parse(self, response):
        item =DoubanItem()
        selector = Selector(response)
        for sel in selector.xpath('//div[@class="info"]'):
            item['title'] =sel.xpath('div[@class="hd"]/a/span/text()').extract()[0]
            # item['link'] = sel.xpath('div[@class="hd"]/a/@href').extract()[0]
            # item['star'] = sel.xpath('div[2]/div/span/text()').extract()[0]
            # item['num'] = sel.xpath('div[2]/div/span/text()').extract()[1]
            # item['actor'] = sel.xpath('div[2]/div/p/text()').extract()[0]
            yield item  # 下一页
            # next_link = selector.xpath('//span[@class="next"]/a/@href').extract()[0]
            # if next_link:
            #     print(next_link)
            # yield Request(self.start_urls[0] + next_link, self.parse)