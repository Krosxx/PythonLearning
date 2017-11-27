import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "***", "***", "webtest")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 数据库插入操作
insertSql="""insert into table1(name,description) VALUES('name','描述')"""

try:
    cursor.execute(insertSql)
    db.commit()
    print("insert成功")
except:
    print()
    print("insert失败")
    db.rollback()


selectSql="select * from table1"
cursor.execute(selectSql)
for result in cursor.fetchall():
    print(result[1])



db.close()
