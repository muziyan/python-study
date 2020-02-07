import pymysql
import pandas as pd
import json

# localhost = ip 地址
# root = 连接用户名
# "" = 连接密码
# python = 数据库名称
db = pymysql.connect("localhost", "root", "", "python",charset="utf8")

# create a cursor 游标对象 相当于php的pdo
# cursor = db.cursor()
# 指定返回数据类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

# 插入假数据
'''
sql = "insert into `test` (title) values('测试文章{}')"
# 生成假数据sql list
sql_list = [sql.format(i) for i in range(100)]

for sql in sql_list:
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
'''

# 查询所有数据
'''
sql = "select * from test"
cursor.execute(sql)
results = cursor.fetchall()
# 将从数据库里面获取的数据储存在test.json里面
with open("test.json",'w') as f:
    f.write("[")
    i = 0
    for val in results:
        i = i + 1
        f.write(json.dumps(val,indent=2,ensure_ascii=False))
        if i != len(results):
            f.write(",\n")
    f.write("]")
'''

# 查询单个数据
'''
sql = "select * from test where id = 203"
cursor.execute(sql)
result = cursor.fetchone()
print(result)
'''

# 修改数据
'''
sql = "update test set title = '测试文章999' where id = 1"
cursor.execute(sql)
db.commit()
'''

'''
# 删除数据
# 删除单个数据
sql = "DELETE FROM `test` WHERE id = 102"
# 清空整个表
sql = "delete from test"
result = cursor.execute(sql)
db.commit()
print("删除成功" if result else "删除失败")
'''

'''
sql = "select count(*) from test"
cursor.execute(sql)
count = cursor.fetchone()
'''

'''
# 将获取的数据转换成DataFrame类型
sql = "select * from test"
cursor.execute(sql)
# 获取数据库列表信息
col = cursor.description
print(col)
# 获取全部查询信息
result = cursor.fetchall()
# 获取的信息默认为tuple类型，讲columns转换成DataFrame类型
# list(tuple) 是将tuple =》 list
columns = pd.DataFrame(list(col))
# 将数据转换成DataFrame类型，并匹配columns
df = pd.DataFrame(list(result),columns=columns[0])
'''

# 检测变量类型function
def typeof(variate):
    type = None
    if isinstance(variate, int):
        type = "int"
    elif isinstance(variate, str):
        type = "str"
    elif isinstance(variate, float):
        type = "float"
    elif isinstance(variate, list):
        type = "list"
    elif isinstance(variate, tuple):
        type = "tuple"
    elif isinstance(variate, dict):
        type = "dict"
    elif isinstance(variate, set):
        type = "set"
    return type

