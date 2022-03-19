import sqlite3,time
conn = sqlite3.connect('attendance.db')
cur = conn.cursor()

def get_att(ID):
    q = f"select * from detail where id = '{ID}'"
   
    cur.execute(q)
    for data in cur:
        print(data[0], time.ctime(float(data[1])))
while 1:
    ID  = input("Enter ID ")
    get_att(ID)