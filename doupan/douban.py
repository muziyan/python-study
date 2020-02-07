import json
import requests
from doupan.parse import parse_url




# url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%96%9C%E5%89%A7&sort=recommend&page_limit=20&page_start=0"
url = "https://m.douban.com/rexxar/api/v2/movie/suggestion?start=8&count=10&new_struct=1&with_review=1&for_mobile=1"


headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://movie.douban.com/explore"
}

h_str = parse_url(url)
print(h_str)


response = requests.get(url, headers=headers)
json_str = response.content.decode()

ret1 = json.loads(json_str)
print(ret1['items'])



with open("../douban.json", "w") as f:
    # ensure_ascii:让中文显示成中文
    # indent:能够让下一行在上一行的基础上空格
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))
