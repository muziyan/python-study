import requests
from lxml import etree
import json

url = "https://movie.douban.com/"
headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

response = requests.get(url,headers=headers)
html_str = response.content.decode()

# print(html_str)

# 使用etree处理数据
html = etree.HTML(html_str)
# print(html)

# 1.get the URL of all movies
url_list = html.xpath("//div[@id='screening']/div[@class='screening-bd']//li/@data-trailer")
# print(url_list)

# 2.get the image url of all movies
img_list = html.xpath("//div[@id='screening']/div[@class='screening-bd']//li/ul/li/a/img/@src")
# print(img_list)

# 3.需要把每部电影组成一个字典，字段中式电影的重要数据，比如标题，url，图片地址，评论数，评分
# 思路：
    # 1.分组
    # 2.每一组提取数据
ret1 = html.xpath("//div[@id='screening']/div[@class='screening-bd']//li[@class='ui-slide-item']")
# print(ret1)
items = {}
for val in ret1:
    item = {}
    # the obtained data is a list
    title = val.xpath(".//li[@class='title']/a//text()")
    item['title'] = title
    item['url'] = val.xpath(".//li[@class='title']/a/@href")
    item['img'] = val.xpath(".//li[@class='poster']/a/img/@src")
    items[title[0]] = item

json_data = json.dumps(items,ensure_ascii=False,indent=2)

with open("data.json","a") as f:
    f.write("[")
    f.write(json_data)
    f.write(",\n")
    f.write("]")
