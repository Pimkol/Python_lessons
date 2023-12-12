import tkinter as tk

#1
'''
def button_click1():
    label2.config(text='Желтый фон', bg='Yellow')
    window["bg"] = "Yellow"
    label.config(bg='Yellow')

def button_click2():
    window["bg"] = "Green"
    label2.config(text='Зеленый фон', bg='Green')
    label.config(bg='Green')

window=tk.Tk()
window.geometry('200x150')
window.title('Пример')

label=tk.Label(window, text='Нажмите на кнопку')
label.pack()

button=tk.Button(window, text='Нажать', bg='Yellow', command=button_click1)
button.pack()

button2=tk.Button(window, text='Нажать', bg='Green', command=button_click2)
button2.pack()

label2=tk.Label(window, text='')
label2.pack()

button3=tk.Button(window, text='Выход',command=lambda: window.destroy())
button3.pack()

window.mainloop()'''

#2
def edit_on():
    text.configure(state=tk.NORMAL)
    button2.configure(state=tk.ACTIVE)
    button.configure(state=tk.DISABLED)
    label2.configure(text='Редактирование разрешено')


def edit_off():
    text.configure(state=tk.DISABLED)
    button.configure(state=tk.ACTIVE)
    button2.configure(state=tk.DISABLED)
    label2.configure(text='Редактирование запрещено')

window=tk.Tk()
window.geometry('300x300')
window.title('Пример')

label=tk.Label(text='Введите текст в поле ниже. ')
label.pack()
label2=tk.Label(text='Редактирование разрешено')
label2.pack()

text=tk.Text(window, height=5, width=30)
text.pack()

button=tk.Button(window, text='Разрешить редактирование', command=edit_on, state=tk.DISABLED)
button.pack()

button2=tk.Button(window, text='Запретить редактирование', command=edit_off)
button2.pack()

window.mainloop()