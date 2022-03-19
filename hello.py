from tkinter import *
import speech_recognition as sr
from tkinter import filedialog
def show_data():
    global dbtext
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            dbtext.insert(END,text + '\n')
            
            
        
        except:
            #print("Sorry could not recognize what you said")
            pass
def save():
    global dbtext
    tx = dbtext.get(0.0,END)

    filename =  filedialog.asksaveasfilename(initialdir = "/",
                                             title = "Select file",
                                             filetypes = (("text files","*.txt"),
                                                          ("all files","*.*")))
    file = open(filename,'w')
    file.write(tx)
    file.close()

    

def main():
    global dbtext
    root = Tk()
    root.configure(bg = 'black')

    dbtext = Text(root,font  = 40,bg = 'black',fg = 'white')
    dbtext.pack()

    Button(root,text= 'Get TEXT', font = 30,command=show_data).pack(side = LEFT)
    Button(root,text= 'Save',font = 30, command=save).pack()


    root.mainloop()

if __name__ == '__main__':
    main()





