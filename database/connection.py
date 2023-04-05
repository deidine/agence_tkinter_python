import pymysql.cursors
# Connect to the database
def connects():
   return pymysql.connect(host='localhost',user='root',password='',db='agencetk',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
# if CONNECTION:
#     print('ok')
# else :
#     print('non ok')