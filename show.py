from tkinter import *

import mysql.connector
conn1 = mysql.connector.connect(host = 'localhost',
                                user = 'root',
                                password = 'user1234',
                                database = 'PYTHON')
cur1 = conn1.cursor()
def show_data():
    global dbtext
    q = 'select * from student'
    cur1.execute(q)
    for data in cur1:
        dbtext.insert(END,str(data) + '\n\n')


def main(x):
    global dbtext
    root = Tk()

    dbtext = Text(root)
    dbtext.pack()

    show_data()


    root.mainloop()



