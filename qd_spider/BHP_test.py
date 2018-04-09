import requests
from bs4 import BeautifulSoup
import save_to_mongodb

class HtmlParser(object):
    def __init__(self):
        self.outputer = save_to_mongodb.Save_To_MongoDB()
    def parser(self, new_url):
        headers = {
            'Cookie': 'pgv_pvi=9894278144; pgv_si=s6022032384; _csrfToken=6gu2on27wl5JpgN9ohQr0itCdy7yLkf5WZnBlBvd; newstatisticUUID=1493445100_1119407040; stat_gid=8586759563; stat_id24=0,noimg; stat_sessid=19849810832; nread=2; nb=2; ns=2; e1=%7B%22pid%22%3A%22qd_P_rank_01%22%2C%22eid%22%3A%22qd_C60%22%2C%22l1%22%3A5%7D; e2=%7B%22pid%22%3A%22qd_P_dushi%22%2C%22eid%22%3A%22qd_F120%22%2C%22l1%22%3A3%7D; hiijack=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        }
        res = requests.get(new_url, headers=headers, timeout=3)
        soup = BeautifulSoup(res.text, 'lxml')
        ranks = soup.find_all('em', 'number')
        cates = soup.find_all('a', 'type')
        titles = soup.find_all("a", attrs={"class": 'name', "data-bid": True})
        potentials = soup.find_all('td', 'month')
        authors = soup.find_all('a', 'author')
        refreshtimes = soup.find_all('td', 'time')
        for rank, cate, title, potential, author, refreshtime in zip(ranks, cates, titles, potentials, authors,refreshtimes):
            data = {
                'rank': rank.get_text(),
                'cate': cate.get_text(),
                'title': title.get_text(),
                'potential': potential.get_text(),
                'author': author.get_text(),
                'refreshtime': refreshtime.get_text()
            }
            print(data)
            self.outputer.save_mongo(data)




