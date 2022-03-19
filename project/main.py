import sqlite3
import time
import cv2
from django.template import Engine
import pyttsx3
conn = sqlite3.connect('attendance.db')
cur = conn.cursor()

q = '''create table if not exists detail (
    id text,
    datetime text
) '''


cur.execute(q)
conn.commit()


def set_att(ID):
    q = """insert into detail values (?,?)"""
    cur.execute(q, (ID,str(time.time())))
    conn.commit()

def get_att(ID):
    q = f"select * from detail where id = '{ID}'"
   
    cur.execute(q)
    for data in cur:
        print(data[0], time.ctime(float(data[1])))

# set_att('m1234')
# get_att('m1234')

engine = pyttsx3.init()
engine.setProperty('rate',100)

vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while(True):     

    ret, frame = vid.read()
    ID, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if ID:
        set_att(ID)
        engine.say("welcome "+ID)
        engine.runAndWait()
        time.sleep(2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  

vid.release()

cv2.destroyAllWindows()