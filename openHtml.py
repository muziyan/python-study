import requests

url = "https://juejin.im/user/5cf01072f265da1bb13f171d/"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
}

Cookie = "b={}; gr_user_id=55be4ee4-926c-44b1-bc51-1fb5f2a17bbf; _ga=GA1.2.1696251501.1580911812; _gid=GA1.2.667598675.1580911812; gr_session_id_89669d96c88aefbc=77fddefa-b65c-4254-aad3-e35234e78353; Hm_lvt_93bbd335a208870aa1f296bcd6842e5e=1580911811,1580915242; gr_session_id_89669d96c88aefbc_77fddefa-b65c-4254-aad3-e35234e78353=true; auth=eyJ0b2tlbiI6ImV5SmhZMk5sYzNOZmRHOXJaVzRpT2lKU1RsaHpTbWQ0VUZWclluTjNRMU4xSWl3aWNtVm1jbVZ6YUY5MGIydGxiaUk2SWxCRlV6RTRTMGRHTVZCWVdtTm5ZVm9pTENKMGIydGxibDkwZVhCbElqb2liV0ZqSWl3aVpYaHdhWEpsWDJsdUlqb3lOVGt5TURBd2ZRPT0iLCJjbGllbnRJZCI6MTU4MDkxNTM3MjY3OSwidXNlcklkIjoiNWNmMDEwNzJmMjY1ZGExYmIxM2YxNzFkIn0=; auth.sig=kkrGnEDF0c0LBRSU30eM6RgodxQ; gr_cs1_77fddefa-b65c-4254-aad3-e35234e78353=objectId%3A5cf01072f265da1bb13f171d; Hm_lpvt_93bbd335a208870aa1f296bcd6842e5e=1580915513; QINGCLOUDELB=229d9a3634d498216e02f8b4f3770be609f51ba16147f64a21f5d51a89fcd206|Xjrb+|Xjrb+"

cookie_dict = {i.split("0")[0]: i.split("=")[-1] for i in Cookie.split("; ")}

print(cookie_dict)

response = requests.get(url, headers=headers,cookies=cookie_dict)

with open("renren.html", "w") as f:
    f.write(response.content.decode())
