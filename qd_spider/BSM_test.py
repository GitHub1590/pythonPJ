import BHP_test
import BUM_test

class SpiderMain(object):
# 类的初始化，将要用到的其他几个模块的类进行初始化
    def __init__(self,main_url):
        self.url = BUM_test.UrlManager()
        self.parser = BHP_test.HtmlParser()
#构造SpiderMain类的属性，用url管理器的get_ul_list方法得到
        self.url_list = self.url.get_url_list(main_url)
# 构造主程序的craw方法
    def craw(self, root_url):  # 构造主程序craw方法,爬虫调度程序
        count = 1
        url_max = self.url.urls_max
        while   self.url.has_new_url():  # 爬虫循环
            new_url = self.url.get_new_url()  # 获取待爬取的url
            # print('craw{0}: {1}'.format(count, new_url),"\n")
            # result = self.parser.parser(new_url)
            # db[MONGO_TABLE].insert(result)
            self.parser.parser(new_url)
            count = count +1
            if count > url_max:
                break

if __name__ == "__main__":
    # main_url =  str(input("将你要分析的榜单首页链接复制进来\n》》》在这里输入："))
# 将爬虫主程序的类进行实例化
    main_url = "http://r.qidian.com/signnewbook?style=2"
    OSP = SpiderMain(main_url)
    url_list = OSP.url_list
# 使用爬虫主程序中的craw方法开始爬取数据
    result = OSP.craw(main_url)


