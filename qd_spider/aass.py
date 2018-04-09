from lxml import etree
import requests
from bs4 import BeautifulSoup
headers = {
            'Cookie': 'pgv_pvi=9894278144; pgv_si=s6022032384; _csrfToken=6gu2on27wl5JpgN9ohQr0itCdy7yLkf5WZnBlBvd; newstatisticUUID=1493445100_1119407040; stat_gid=8586759563; stat_id24=0,noimg; stat_sessid=19849810832; nread=2; nb=2; ns=2; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C60%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_dushi%22%2C%22eid%22%3A%22qd_F120%22%2C%22l1%22%3A3%7D; hiijack=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        }
# 请求到的结果
res = requests.get('http://r.qidian.com/signnewbook?style=2&page=1', headers=headers)
res1 =res.text
# 对结果进行解析
#         soup = BeautifulSoup(res.text, 'lxml')
# # 定位到总页面数的标签
#         tps = soup.find_all(attrs={'data-pagemax': True})[0]
# # 从标签中取出最大页面数的属性值
#         urls_max = int(tps.attrs['data-pagemax'])
T = etree.HTML(res1)
# T.xpath('//*[@id="rank-view-list"]/div/table/tbody/tr/@')[0]
print(T.xpath('//*[@id="page-container"]/@data-pagemax')[0])