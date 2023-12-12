import tkinter as tk

def button_click():
    label.config(text='Теперь кликните в роизвольном месте')

def canvas_clic(event):
    x,y=event.x, event.y
    label.config(text=f'произведен щелчек мышью по координатам: \n({x}, {y})')

window=tk.Tk()
window.geometry('300x300')
window.title('Пример')

label=tk.Label(window, text='Нажмите на кнопку')
label.pack()

button=tk.Button(window, text='Нажать', command=button_click)
button.pack()

canvas=tk.Canvas(window, width=200, height=200)
canvas.pack()

canvas.bind('<Button-1>', canvas_clic)

button2=tk.Button(window, text='Выход',command=lambda: window.destroy())
button2.pack()

window.mainloop()