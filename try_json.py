import requests

query = input("请输入要翻译的中文:")

print(query)

url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

headers = {
    "User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Cookie":"BIDUPSID=038998BCB4C7D950B152EF443E1B68A8; PSTM=1580902106; BAIDUID=038998BCB4C7D950373D357FF646FA57:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1456_21082_30717; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1580911736; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1580912058; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1580910798,1580910823,1580987476; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1580987476; __yjsv5_shitong=1.0_7_c9340d2ceb1fb9f5b7387a9672e9df40bd27_300_1580987514824_116.136.20.184_2414d5c9; yjs_js_security_passport=857777709a71eb2cca7bff5ef4b8c63116786824_1580987526_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
}

data = {
    "from": "zh",
    "to": "en",
    "query": query,
    "token":"f8ee45884688b3150ea7b1f8a3c78517"
}

print(data)

response = requests.post(url, headers=headers, data=data)

print(response)

html_str = response.content.decode()

print(html_str)


