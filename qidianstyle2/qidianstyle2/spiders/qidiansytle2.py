from scrapy import Request
from scrapy import Spider
from qidianstyle2.items import Qidianstyle2Item

class QiDianSpider(Spider):
    name = 'qidianST2'
    start_urls= ['http://r.qidian.com/signnewbook?style=2']

    def parse(self, response):
        base_url = 'http://r.qidian.com/signnewbook?style=2&page={}'
        url_max = int(response.xpath('//*[@id="page-container"]/@data-pagemax').extract()[0])
        for s in range(1,url_max+1):
            yield Request(base_url.format(s),callback=self.parse_pagedetail)

    def parse_pagedetail(self, response):
        item = Qidianstyle2Item()
        for sel in response.xpath('//*[@id="rank-view-list"]/div/table/tbody/tr'):
            item['rank'] = sel.xpath('td/em/span/text()').extract()[0]
            item['cate'] = sel.xpath('td//a/text()').extract()[0]
            item['author'] = sel.xpath('td/a/text()').extract()[3]
            item['title'] = sel.xpath('td/a/text()').extract()[1]
            item['freshtime'] = sel.xpath('td/text()').extract()[1]
            yield item  # 下一页
