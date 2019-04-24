
import MySQLdb

# 连接数据库         连接地址        账号      密码             数据库             数据库编码
db = MySQLdb.connect("localhost", "root", "123456", "tcm_clinicaltttpart_pure", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "select * from rules_of_treatment"

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      parent_id = row[1]
      content = row[2]
      content_unit = row[3]
      order_num = row[4]
      create_time = row[5]
      create_user = row[6]
      remark = row[7]
      # 打印结果
      print("id=%s, parent_id=%s, content=%s, content_unit=%s, order_num=%s, create_time=%s, create_user=%s, remark=%s " % (id, parent_id, content, content_unit, order_num, create_time, create_user, remark ))
except:
   print("Error: unable to fecth data")

# 关闭数据库连接
db.close()

