# Tkinter Dictionary
Welcome to the exciting world of GUI programming with Tkinter. This project aims at getting you acquainted with Tkinter, the built-in graphical user interface (GUI) interface for all standard Python distributions.

## 1. Preliminary 
![](https://devngecu.herokuapp.com/media/photos/2020/06/10/preliminaries.png)


Tkinter is suited for application to a wide variety of areas ranging from small desktop applications, to use in scientific modeling and research endeavors across various disciplines.The purpose of this project is to make you comfortable with Tkinter. It aims at introducing you to various components of GUI programming with TkinterBy the end of this project, you will have developed several partly functional dummy applications such as the one shown as follows
![](https://devngecu.herokuapp.com/media/photos/2020/06/10/developer.png)

The features that make Tkinter a great choice for GUI programming include:-
⋅⋅* It is simple to learn (simpler than any other GUI package for Python)
⋅⋅* Relatively little code can produce powerful GUI application
⋅⋅* Layered design ensures that it is easy to graspfIt is portable across all operating systemsfIt is easily accessible as it comes pre-installed with standard Python distribution
⋅⋅* None of the other GUI toolkits has all of these features at the same time.

To test if you have the correct Tkinter version on your Python installation, type the following commands in your IDE:
```python
import tkinter

print(tkinter._test())
```
This should pop up a window where the first line in the window reads This is Tcl/Tk version 8.5.

We will begin with what we will require for this breif project:

1. JSON File - Which acts as the source of data having names as keys and the definitions as value

2. A Photo- Which will act as our background
![](https://devngecu.herokuapp.com/media/photos/2020/06/10/WebDevelopemnt.png)

3. Obviously a script for our code


## 2. The root window – your drawing board and its Widgets




GUI programming is an art, and like all art, you need a drawing board to capture your ideas. The drawing board you will use is called the root window. Our first goal is to get the root window ready.

The following screenshot depicts the root window we are going to create:

![](https://devngecu.herokuapp.com/media/photos/2020/06/10/tk.png)

Drawing the root window is easy. You just need the following three lines of code:
```python
from tkinter import *
window = Tk()
window.mainloop()
```
The description of the code is as follows:

The first line imports all (*) classes, attributes, and methods of Tkinter into the current workspace.
The second line creates an instance of the class Tkinter.Tk. This creates what is called the "root" window that you see in the screenshot provided. By convention, the root window in Tkinter is usually called "root", but I named it "window" but are free to call it by any other name.
The third line executes the mainloop (that is, the event loop) method of the rootobject. The mainloop method is what keeps the root window visible. If you remove the third line, the window created in line 2 will disappear immediately as the script stops running. This will happen so fast that you will not even see the window appearing on your screen. Keeping the mainloop running also lets you keep the program running until you press the close button, which exits the main loop

### Widgets – building blocks for your GUI program

Now that we have our Toplevel window ready, it is time to think over the question, what components should appear in the window? In Tkinter jargon, these components are called widgets

The syntax for adding a widget is as follows:
```python
mywidget = Widget-name (its container window,**configuration options)
```
In the following example below, we will add two widgets, a label and a button, to the root frame. Notice how all widgets are added in between the skeleton code we defined in the first example.
```python
from tkinter import *
window = Tk() 
label = Label(window,text="I am a label widget") 
b1 = Button(root,text="I am a button") 
label.pack()
b1.pack()
window.mainloop()
```
The format for adding widgets is the same . To give you a flavor, here's some sample code for adding some common widgets:

Label(parent, text=" Enter your Password:")

Button(parent, text="Search")

Checkbutton(parent, text='RememberMe', variable=v, value=True)

Entry(parent, width=30)Radiobutton(parent, text=Male, variable=v, value=1)

Radiobutton(parent, text=Female, variable=v, value=2)

OptionMenu(parent, var, "Select Country", "USA", "UK", "India", Others")

Scrollbar(parent, orient=VERTICAL, command=mytext.yview)

Hope you can spot the pattern common to each widget?

For our case,we will be using the Entry,Button,Text widgets:

```python
e1 = Entry(window,textvariable="")

b1 = Button(window,text="Search")

t1 = Text(window)
```
 Let us now turn our attention to the second component of GUI programming—the question of where to place those widgets.This is taken care of by the geometry manager options of Tkinter. This component of GUI programming involves deciding the position of the widget, overall layout, and relative placement of various widgets on the screen.

The geometry managers are as follows:

    pack: Simple to use for simpler layouts but may get very complex for slightly complex layouts.
    grid: This is the most commonly used geometry manager that provides a table-like layout of management features for easy layout management.
    place: This is least popular, but provides the best control for absolute positioning of widgets.

I'll focus on pack and place since they are the only ones i'll be using.

The pack geometry derives its name from the fact that it literally packs widgets on a first-come-first-serve basis in the space available in the master frame in which widgets are pushed.The pack geometry manager fits "slave widgets" into "parent spaces". When packing the slave widgets, the pack manager distinguishes between three kinds of spaces:

The unclaimed space,The claimed but unused space,The claimed and used space

I'll not go over them,for more infor,read more on that

The place geometry manager is the most rarely used geometry manager in Tkinter. Nevertheless, it has its uses in that it lets you precisely position widgets within its parent frame using the X-Y coordinate system.The place manager can be assessed using the place() method on all standard widgets.The important options for place geometry include:fAbsolute positioning (specified in terms of x=N or y=N)fRelative positioning (key options include relx, rely, relwidth, and relheight)Other options commonly used with place() include width and anchor (the default is NW)

So lets place our widgets to our main root frame

```python
e1 = Entry(window,textvariable="")
e1.place(relx=.185,rely=0.70,relwidth=.63,relheight=.082)


b1 = Button(window,text="Search")
b1.place(relx=.40,rely=.85,relwidth=.2,relheight=.052)


t1 = Text(window)
t1.place(relx=.185,rely=.05,relwidth=.63,relheight=.20)
```


So far, we have have relied on Tkinter to provide specific platform-based styling for our widgets. However, you can specify your own styling of widgets in terms of their color, font size, border width, and relief

Recall that we could specify widget options at the time of its instantiation as shown:

   mybutton = Button(parent, **configuration options)

Alternatively, you could specify widget options using configure ():

   mybutton.configure(**options)

Styling options are also specified as options to the widgets, either at the time of instantiation or later using the configure option

```python
e1 = Entry(window,textvariable="",bg="#FFFD38",fg="black",justify = CENTER,font = ('courier', 30, 'bold'))
e1.place(relx=.185,rely=0.70,relwidth=.63,relheight=.082)



b1 = Button(window,text="Search",relief=FLAT,bg="green",fg="white",font = ('courier', 30, 'bold') )
b1.place(relx=.40,rely=.85,relwidth=.2,relheight=.052)


t1 = Text(window,fg="white",relief=FLAT,bg="#444444",font = ('courier', 20, 'bold'))
t1.place(relx=.185,rely=.05,relwidth=.63,relheight=.20)
```

Now that we are done discussing styling options, let us wrap up with a discussion on some commonly used options for the root window:





| Method        | Description
| ------------- |:-------------:| -----:|
| root.title("title of my program")| 	Specifying the title for the Title bar
| root.geometry('142x280+150+200') )      | 	You can specify the size and location of a root window using a string of the form widthxheight + xoffset + yoffset      |    |

For our case we will require the title only:-

```python
window.title (" DevNgecu Dictionary")
```

## 3. Window Background

![](https://devngecu.herokuapp.com/media/photos/2020/06/10/window.png)

This we just be a brief session on how to integrate the photo as our background image:

As mentioned earlir we will require Pillow so
```python
pip3 install Pillow
```
From pillow we will require two modules:
```python
from PIL import Image, ImageTk
```
The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.

The following script loads an image, rotates it 45 degrees, and displays it using an external viewer (usually xv on Unix, and the Paint program on Windows).
```python
from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()
```
The ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL images.

A Tkinter-compatible photo image. This can be used everywhere Tkinter expects an image object
```python
class PIL.ImageTk.PhotoImage(image=None, size=None, **kw)
```
For our case:
```python
image = Image.open('WebDevelopemnt.png')
photo_image = ImageTk.PhotoImage(image)
```
To display the background image,we will take a label widget,assign it the image and place it with the pack geometry.As we mentioned in the previous slide,this geometry packs widgets on a first-come-first-serve basis in the space available in the master frame in which widgets are pushed.So it should come before the rest of the widgets

Now all is remaining is the functionality part,See you in the next slide

## 3. Functonality
![](https://devngecu.herokuapp.com/media/photos/2020/06/10/FUN.png)

In this slide will load data from our json file and check on the proximity of word to define.With that we will need two libraries which we previously mentioned: JSON,difflib.So lets first load the data
```python
import json
data = json.load(open("data.json"))
from difflib import get_close_matches
```
The get_close_matches finds all close matches of input string from a list.difflib.get_close_matches(word, possibilities, n, cutoff) accepts four parameters in which n, cutoff are optional. word is a sequence for which close matches are desired, possibilities is a list of sequences against which to match word. Optional argument n (default 3) is the maximum number of close matches to return, n must be greater than 0. Optional argument cutoff (default 0.6) is a float in the range [0, 1]. Possibilities that don’t score at least that similar to word are ignored.

Next is the search function that will check for the name we desire
```python
def search(word):
    if word in data:
        t1.delete(1.0,END)
        t1.config(fg='white')
        t1.insert(END,data[word])
    elif len(get_close_matches(word,data.keys()))>0:
        t1.config(fg='red')
        t1.delete(1.0,END)
        t1.insert(END,"Did you mean {} to mean : {} ".format (get_close_matches(word,data.keys())[0],data[get_close_matches(word,data.keys())[0]]))
        output = get_close_matches(word,data.keys())
```
The description of the code is as follows:

The function will pass in the word being searched as a its paramenter
We check if the word is in the data source.if so:-
    delete any content in the text area widget."1.0" and "end" refer to the first character and the last character of the contents in the Text widget
    color the text content white meaning it is successfull
    Then append the definitions to the text area widget
If there is no such word check if there are close matches of the word and:
    color the text area content red meaning that there was an error
    Delete any content in the text area widget."1.0" and "end" refer to the first character and the last character of the contents in the Text widget
    Then append the question "Did you mean: Y:X".in this context Y gets the closest word that ryhms with the typed word.eg.rainn-->rain.X is the definition of Y

By Y we mean the firt word in the matches provided hence the code:

```python
get_close_matches(word,data.keys())[0]
```

This is so since,the best (no more than n) matches among the possibilities are returned in a list, sorted by similarity score, most similar first.

```
from tkinter import *

import json

from difflib import get_close_matches



data = json.load(open("data.json"))



def search(word):

    if word in data:

        t1.delete(1.0,END)

        t1.config(fg = "white")

        t1.insert(END,data[word])

    elif len(get_close_matches(word,data.keys()))>0:

        t1.config(fg = "red")

        t1.delete(1.0,END)

        t1.insert(END,"Did you mean {} to mean : {} ".format (get_close_matches(word,data.keys()[0]),data[get_close_matches(word,data.keys())[0]]))

        output = get_close_matches(word,data.keys())



window = Tk()

window.title("Dictionary")



#Input(Entry)

ntry_value = StringVar()

ntry = Entry(window,textvar = ntry_value,font = ('times',20,'bold'))

ntry.place(relx = .185,rely = 0.70,relwidth = .63,relheight = .082)



#Search button

btn = Button(window,text = "Search",command = lambda : search(ntry_value.get()),font = ('times',15,'bold'))

btn.place(relx=.40,rely=.85,relwidth=.2,relheight=.052)



#output the definition of the word

t1 = Text(window,font = ('times',15,'bold'))

t1.place(relx = .185,rely = .05,relwidth = .63,relheight = .20)



window.mainloop()
```
