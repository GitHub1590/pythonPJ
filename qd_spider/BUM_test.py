import requests
from lxml import etree
from bs4 import BeautifulSoup
# 构造url管理器类
class UrlManager(object):

# 类的实例化，确定类的基本属性
    def __init__(self):
# new_urls属性（集合），用来做新url管理
        self.new_urls = set()
# old_url属性(集合)，用来管理已经爬的url
        self.old_urls = set()
# url_list属性（集合），用来存储要爬榜单主页中确定的待爬取总页数所构造出的url_list(url列表)
        self.url_list = []
        self.url_max = str()

# 构造url管理器的第一个方法——待爬取url列表生成器
    def get_url_list(self, main_url):
# 头文件
        self.headers = {
            'Cookie': 'pgv_pvi=9894278144; pgv_si=s6022032384; _csrfToken=6gu2on27wl5JpgN9ohQr0itCdy7yLkf5WZnBlBvd; newstatisticUUID=1493445100_1119407040; stat_gid=8586759563; stat_id24=0,noimg; stat_sessid=19849810832; nread=2; nb=2; ns=2; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C60%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_dushi%22%2C%22eid%22%3A%22qd_F120%22%2C%22l1%22%3A3%7D; hiijack=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        }
# 请求到的结果
        res = requests.get(main_url, headers=self.headers)
# 对结果进行解析
        soup = BeautifulSoup(res.text, 'lxml')
# # 定位到总页面数的标签
        tps = soup.find_all(attrs={'data-pagemax': True})[0]
# # 从标签中取出最大页面数的属性值
        urls_max = int(tps.attrs['data-pagemax'])
#         T = etree.HTML(res)
#         urls_max = T.xpath('//*[@id="rank-view-list"]/div/table/tbody/tr')
        self.urls_max = urls_max
#构造待爬取url列表
        urls_list = ["http://r.qidian.com/signnewbook?style=2&page={0}".format(str(i)) for i in range(1, urls_max + 1)]
# 将分析出来的待爬列表传递给类属性self_url_list
        self.url_list.extend(urls_list)
# 将self.url_list进行倒序，作为栈结构
        self.url_list.reverse()
        new_url_list = self.url_list
        print(new_url_list)

# 构造url管理器的第二个方法，判断带爬url列表时候还存在未爬取的url
    def has_new_url(self):
        return len(self.url_list) != 0

# 构造url管理器的第三个方法，从待爬列表生成器中一个个取出要爬取的url
    def get_new_url(self):
        new_url = self.url_list.pop()  # 取得新的url，并将取出的url从url列表中删除
        self.old_urls.add(new_url)  # 将已经爬取的url放到old_urls列表中，即已爬取url列表
        return new_url  # 将这个取出的url返回，交给网页下载器
