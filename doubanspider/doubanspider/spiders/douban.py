from scrapy import Request
from scrapy import Selector
from scrapy import Spider
from doubanspider.items import DoubanspiderItem


class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ["movie.douban.com"]
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        item =  DoubanspiderItem()
        selector = Selector(response)
        for sel in selector.xpath('//div[@class="info"]'):
            item['chinese_title'] = sel.xpath('div[@class="hd"]/a/span/text()').extract()[0]
            item['other_title'] = sel.xpath('div[@class="hd"]/a/span/text()').extract()[1]
            item['link'] = sel.xpath('div[@class="hd"]/a/@href').extract()[0]
            item['star'] = sel.xpath('div[2]/div/span/text()').extract()[0]
            item['num'] = sel.xpath('div[2]/div/span/text()').extract()[0]
            item['actor']= sel.xpath('string(//*[@id="content"]/div/div/ol/li/div/div[2]/div/p[1]/text()[1])').extract()[0]
            yield item  # 下一页
        # for sel in selector.xpath('//div[@class="info"]'):
        #     item['chinese_title'] = sel.xpath('div[@class="hd"]/a/span/text()').extract()
        #     item['other_title'] = sel.xpath('div[@class="hd"]/a/span/text()').extract()
        #     item['link'] = sel.xpath('div[@class="hd"]/a/@href').extract()
        # #     item['star'] = sel.xpath('div[2]/div/span/text()').extract()
        # #     item['num'] = sel.xpath('div[2]/div/span/text()').extract()
        # #     item['actor']= sel.xpath('string(//*[@id="content"]/div/div/ol/li/div/div[2]/div/p[1]/text()[1])').extract()
        # #     yield item  # 下一页
            next_link = selector.xpath('//span[@class="next"]/a/@href').extract()[0]
            if next_link:
                print(next_link)
            yield Request(self.start_urls[0] + next_link, self.parse)