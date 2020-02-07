### python操作MySQL数据库
####具体增删改查操作在mysql.py里面有注释和操作
- 1.先使用`pip3 install PyMySql`安装`pymysql`
- 2.使用`import pymysql`导入
- 3.连接数据库  
    `db = pymysql.connect("localhost", "username", "password", "dbname")`
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
  