### 写爬虫的套路
- 1.url
    - 知道url地址的规律和总得页码数：构造url地址的列表
    - start_url
- 2.发送请求,获取响应
    - requests
- 3.提取数据
    - 返回json字符串：json模块
    - 返回的是html字符串：lxml模块配合xpath提取数据
- 4.保存
