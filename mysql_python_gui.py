from tkinter import *
import show
import mysql.connector
conn = mysql.connector.connect(host = 'localhost',
                                user = 'root',
                                password = 'user1234',
                                database = 'PYTHON')
cur = conn.cursor()


def insert_into_table():
    name_ = name.get()
    Id_ = int(Id.get())
    sub1_ = float(sub1.get())
    sub2_ = float(sub2.get())
    sub3_ = float(sub3.get())
    print(name_,Id_,sub1_,sub2_,sub3_)
    name.delete(0 , END)
    Id.delete(0 , END)
    sub1.delete(0 , END)
    sub3.delete(0 , END)
    sub2.delete(0 , END)

    sql = "INSERT INTO student (id ,name,sub1,sub2,sub3) VALUES (%s, %s,%s, %s, %s)" 
    val = (Id_,name_,sub1_,sub2_,sub3_)
    cur.execute(sql, val)
    conn.commit()








win  = Tk()
win.geometry('500x400')
win.resizable(False,False)
win.configure(background='black')
Label(win, text = "Student Detail",bg='black',fg='white',font = 20).grid(row=0,column=1,columnspan=5)

Label(win, text = "Name",bg='black',fg='white',font = 20).grid(row=1,column=0,sticky=W)
Label(win, text = "Id",bg='black',fg='white',font = 20).grid(row=2,column=0,sticky=W)

Label(win, text = "Subject 1",bg='black',fg='white',font = 20).grid(row=3,column=0)
Label(win, text = "Subject 2",bg='black',fg='white',font = 20).grid(row=4,column=0)
Label(win, text = "Subject 3",bg='black',fg='white',font = 20).grid(row=5,column=0)

name = Entry(win,font = 20)
name.grid(row=1,column=1,ipadx=2)

Id = Entry(win,font = 20)
Id.grid(row=2,column=1,ipadx=2)

sub1 = Entry(win,font = 20)
sub1.grid(row=3,column=1,ipadx=2)


sub2 = Entry(win,font = 20)
sub2.grid(row=4,column=1,ipadx=2)



sub3 = Entry(win,font = 20)
sub3.grid(row=5,column=1,ipadx=2)

Button(win,text = "Submit" , font = 25,bd = 5,command=insert_into_table).grid(row=6,column=1,ipady=5)

bt = Button(win,text = "Get data" , font = 25,bd = 5)
bt.grid(row=6,column=0,ipady=5)


bt.bind('<Button-1>', show.main)
l = ['#ff4d4d','#006bb3','#00b300']
import random
bt.bind('<Motion>', lambda x : bt.configure(bg = random.choice(l)))

win.mainloop()