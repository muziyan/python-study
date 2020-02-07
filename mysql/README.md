### python操作MySQL数据库
##### 具体增删改查操作在mysql.py里面有注释和操作
- 1.先使用`pip3 install PyMySql`安装`pymysql`
- 2.使用`import pymysql`导入
- 3.连接数据库  
    `db = pymysql.connect("localhost", "username", "password", "dbname",charset="utf8")`
    - `localhost`是主机地址
- 4.生成一个浮标实例  
    `cursor = db.cursor()`
- 5.所有增删该查必须使用浮标实例的`execute`方法
    ```
    sql = "select * from "
    cursor.execute(sql)
    ```
  - 获取查询的数据
    ```
    cursor.fetchall() # 这是获取所有数据
    cursor.fetchone() # 这是获取一个数据
    ```
  - 执行增加或者删除操作必须在后面执行一次`db.commit()`数据库才会发生改变  
      ```
      sql = "delete from tablename"
      cursor.execute(sql)
      db.commit()        
      ```

### 将mysql返回的数据转换成DataFrame类型方便操作  
    需要安装Pandas`pip3 install Pandas`
    # 引入pandas模块
    import pandas as pd
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
