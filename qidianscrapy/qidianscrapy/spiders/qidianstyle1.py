from scrapy import Request
from scrapy import Spider

from qidianscrapy.items import QidianscrapyItem


class QiDianStyle1(Spider):
    name = 'qidianST1'
    start_urls = ['http://r.qidian.com/signnewbook?style=1']

    def parse(self, response):
        base_url = 'http://r.qidian.com/signnewbook?style=1&page={}'
        url_max = int(response.xpath('//*[@id="page-container"]/@data-pagemax').extract()[0])
        for s in range(1,url_max+1):
            yield Request(base_url.format(s),callback=self.parse_pagedetail)

    def parse_pagedetail(self, response):
        item = QidianscrapyItem()
        for sel in response.xpath('//*[@id="rank-view-list"]/div/ul/li'):
            item['rank'] = sel.xpath('div[@class="book-img-box"]/span/text()').extract()[0]
            item['cate'] = sel.xpath('div[@class="book-mid-info"]/p[@class="author"]/a/text()').extract()[1]
            item['author'] = sel.xpath('div[@class="book-mid-info"]/p[@class="author"]/a/text()').extract()[0]
            item['title'] = sel.xpath('div[@class="book-mid-info"]/h4/a/text()').extract()[0]
            item['freshtime'] = sel.xpath('div[@class="book-mid-info"]/p[@class="update"]/span/text()').extract()[0]
            yield item  # 下一页
