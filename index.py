from tkinter import *
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    if word in data:
        t1.delete(1.0,END)
        t1.config(fg='blue')
        listboxA.delete(0,END)
        listboxA.insert(0,'Meaning found')
        listboxA.config(fg='green')
        t1.insert(END,data[word])
    elif len(get_close_matches(word,data.keys()))>0:
        t1.config(fg='red')
        t1.delete(1.0,END)
        t1.insert(END,"Did you mean {} to mean : {} ".format (get_close_matches(word,data.keys())[0],data[get_close_matches(word,data.keys())[0]]))
        listboxA.delete(0,END)
        output = get_close_matches(word,data.keys())
        for item in output:
            listboxA.insert(0,item)


#main window
window = Tk()
window.title (" DevNgecu Dictionary")
window.geometry("500x500+350+100")
window.config(bg='#343434')

def close():
    window.destroy()
  
#label for the word to search
l1 = Label(window,text="Name")
li.config(bg='#343434',fg='white')
l1.place(relx=0,rely=0.005,relwidth=0.1)


#input of the word to search
e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value,cursor="circle")
e1.place(relx=.1,rely=0.005,relwidth=.8)

#label for the word to search
l2 = Label(window,text="Definition")
l2.config(bg='#343434',fg='white')
l2.place(relx=0,rely=.1,relwidth=0.1)


#seach button to execute command

b1 = Button(window,text="Search",command= lambda : search(e1_value.get()),relief=RIDGE )
b1.place(relx=.1,rely=.9,relwidth=.3,height=45)


#Close Button
b2 =Button(window,text="Close",command=close,relief=RIDGE )
b2.place(relx=.6,rely=.9,relwidth=.3,height=45)

#ouput the definition of the word
t1 = Text(window,fg="blue",relief=FLAT)
t1.place(relx=0.1,rely=0.1,relwidth=.5)

listboxA = Listbox(window,selectbackground="red")
listboxA.place(relx=0.7,rely=.1,relwidth=.2,relheight=.78)

for key in data:
    listboxA.insert(END, key)


window.mainloop()