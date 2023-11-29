import MySQLdb
import sys 
# Open database connection 
username = sys.argv[1]
password = sys.argv[2]
namebdd = sys.argv[3]
db = mysql.connect(host="localhost",user=username,password=password,database=namebdd) 
cursor = db.cursor()
sql = "SELECT * FROM states ORDER BY states.id ASC"
cursor.excute(sql)
# disconnect from server 
db.close() 
