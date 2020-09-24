import pymysql
import pandas as pd
dbConn = pymysql.connect(user='######', passwd='######', host='######', db='iris', charset='utf8')
cursor = dbConn.cursor(pymysql.cursors.DictCursor)
sql = "select count(*) from dataset;"
cursor.execute(sql)
result = cursor.fetchall()
#print(result)
print(result[0]['count(*)'])

sql = "select a.SL, a.SW, a.PL, a.PW, b.Species_name from dataset a " \
      "left join flower b on a.species = b.species;"
cursor.execute(sql)
result = cursor.fetchall()
result = pd.DataFrame(result)
#print(result)
