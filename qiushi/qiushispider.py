# coding = utf-8
import requests
import json
from lxml import etree


class QiushiSider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/hot/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        html_str = response.content.decode()
        return html_str

    def get_url_list(self):  # 1.根据url地址的规律，构造url list
        url_list = [self.url_temp.format(i) for i in range(1, 14)]
        return url_list

    def get_content_list(self, html_str):  # 3.提取数据
        html = etree.HTML(html_str)
        # 1.分组
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            # item['author_name'] = div.xpath(".//h2/text()")[0]
            item['author_name'] = div.xpath(".//h2/text()")[0].strip() if len(div.xpath(".//h2/text()")) > 0 else None
            item['content'] = div.xpath(".//div[@class='content']/span/text()")
            item['content'] = [i.strip() for i in item['content']]
            item['stats_vote'] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item['stats_vote'] = item['stats_vote'][0] if len(item['stats_vote']) > 0 else None
            item['stats_comments'] = div.xpath(".//span[@class='stats-comments']/a/i/text()")
            item['stats_comments'] = item['stats_comments'][0] if len(item['stats_comments']) > 0 else None
            item['img'] = div.xpath("./div[@class='thumb']//img/@src")
            item['img'] = "https:" + item['img'][0] if len(item['img']) > 0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        with open("qiubai.txt", 'a') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功!")

    def run(self):
        # 1.根据url地址的规律，构造url list
        url_list = self.get_url_list()
        # 2.发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list=content_list)


if __name__ == "__main__":
    qiushi = QiushiSider()
    qiushi.run()
