import pyttsx3,os
import speech_recognition as sr
import webbrowser
engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()


def search(data):
    
    #if data.split().lower() in data.lower():
        #webbrowser.open('https://en.wikipedia.org/wiki/India')
    webbrowser.open(f'https://en.wikipedia.org/wiki/{data.split()[-1].lower()}')

def windows():
    webbrowser.open
while 1:
    with mic as source:
        print('   you Say ')
        audio = r.record(source,duration = 4)
    data = r.recognize_google(audio)
    print('Out >>> ',data)
    data = data.lower()
    if ('search' in data) or ('url' in data):search(data)
    if 'calculator' in data:
        os.system('calc')
        
    if 'notepad' in data:
        webbrowser.open(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk")
    elif data == 'stop':break
        
    

