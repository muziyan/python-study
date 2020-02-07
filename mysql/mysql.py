import pymysql as sql

# localhost = ip 地址
# root = 连接用户名
# "" = 连接密码
# python = 数据库名称
db = sql.connect("localhost", "root", "", "python")

# create a cursor 游标对象 相当于php的pdo
cursor = db.cursor()


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
print(results)
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
