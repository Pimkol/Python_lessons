from tkinter import *
from tkinter.filedialog import asksaveasfilename as saveAs
import PIL
from PIL import Image, ImageDraw
from PIL import ImageTk 
from tkinter.messagebox import *
from tkinter.ttk import Combobox 
from tkinter import Tk, Button
from tkinter.colorchooser import askcolor
 
brush_size=3
color='black'
wc = 1000
hc = 650
bg='white'
 

def clear(): 
    cv.delete('all')
    

def paint(e):
    global lastx, lasty
    line_width = choose_size_button.get()
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill=color, width=line_width, capstyle=ROUND, smooth=TRUE, splinesteps=100)
    draw.line((lastx, lasty, x, y), fill=color, width=line_width)
    lastx, lasty = x, y  
 
def paint_rec(e):
    global lastx, lasty
    line_width = choose_size_button.get()
    x, y = e.x, e.y
    cv.create_rectangle((lastx, lasty, x, y), fill=color, width=line_width, capstyle=ROUND, smooth=TRUE, splinesteps=100)
    draw.rectangle((lastx, lasty, x, y), fill=color, width=line_width)
    lastx, lasty = x, y 
     

def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y
      

def color_change():
    global color
    color=askcolor(color=color)[1]  
 
 
def eraser(new_color):
    global color
    color=new_color 
 
    
def about():
    win1=Toplevel(win)
    lab=Label(win1,text='''Тут можно рисовать. Для очистки холста нажмите Файл-очистить. '''
    , width=90, height=25, font='Times 15', fg='Black')
    lab.pack()
    
    
  
def close_win():
    win.destroy()  
                  

win = Tk()
win.title("Snake Paint")
lastx, lasty = None, None
image_number = 0
 
 
cv = Canvas(win, width=wc, height=hc, bg=bg)
image1 = PIL.Image.new('RGB', (wc, hc), bg)
draw = ImageDraw.Draw(image1)
cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)
 

m=Menu(win) 
win.config(menu=m)
fm=Menu(m)
m.add_cascade(label='Файл',menu=fm)
fm.add_command(label="Очистить", command=clear)
fm.add_command(label='Выход', command=close_win)
hm=Menu(m)
m.add_cascade(label='Помощь',menu=hm)
hm.add_command(label='О приложении',command=about)
 

cv.grid(row=2, column=0, columnspan=100, padx=5, pady=5,sticky=E+W+S+N)
 
color_button = Button(win,text='Паллитра', width=10,height=5, command = color_change)
color_button.grid(row=0, column=0)
 
eraser_button = Button(win, text='Ластик', width=10,height=5, command = lambda: eraser('white'))
eraser_button.grid(row=0, column=1)
 
pencil_button = Button(win, text='Кисть', width=10,height=5, command = lambda: eraser('black'))
pencil_button.grid(row=0, column=2)
 
choose_size_button = Scale(win, from_=1, to=100, orient=HORIZONTAL, width=15)  
choose_size_button.grid(row=0, column=3)
 
 
win.mainloop()