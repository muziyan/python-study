import requests
from retrying import retry

'''
专门请求url地址的方法
'''

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://movie.douban.com/explore"
}


@retry(stop_max_attempt_number=3)  # 让被装饰的函数反复执行三次，三次全部报错才会报错，中间又一次正常都返回正常
def _parse_url(url):
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == "__main__":
    url = "http://www.bnaidu.com"
    print(parse_url(url))
