# request module
import requests
# json module
import json
# urllib module
import urllib.parse

'''
url1 = "https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&otf=1&ssel=0&tsel=0&xid=1788074&kc=1&tk=143301.302265&q=%E5%AD%A6%E4%B9%A0"
url2 = "https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=gt&ssel=0&tsel=3&xid=1788074&kc=0&tk=985645.637265&q=%E5%AD%A6%E4%B9%A0"

boolean = url1 == url2
print(boolean)
'''


translate_text = input("请输入需要翻译的文字:")

data = {
    "q": translate_text
}
urlData = urllib.parse.urlencode(query=data)

print(urlData)

# request url
#url="https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=0&tsel=3&xid=1788074&kc=1&tk=614560.1037276&q=%E6%AD%87%E6%81%AF"+urlData
url="https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=0&tsel=3&xid=1788074&kc=1&tk=614560.1037276&"+urlData
print(url)

# request data
# query_string = {
#     ""
# }

# request headers
# forged request
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

# make a request
response = requests.get(url,headers=headers)

# print response status
print(response)

# print response data
json_str = response.content.decode()
print(json_str)


dict_ret = json.loads(json_str)
# print(dict_ret)
dict = dict_ret[0][0][0]
print(dict)




