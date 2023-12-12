import tkinter as tk

#1
'''
def button_clic():
    label.config(text='Кнопка была нажата')

window=tk.Tk()
window.geometry('250x100')
window.title('Пример')

frame = tk.Frame(window, padx = 10, pady = 10)
frame.pack(expand=True)

label=tk.Label(frame, text='Нажмите на кнопку')
label.pack()

button=tk.Button(frame, text='Нажать', command=button_clic)
button.pack()

button2=tk.Button(frame, text='Выход',command=lambda: window.destroy())
button2.pack()

window.mainloop()'''

#2
'''
def clear():
    text=entry.get()
    label.config(text='Вы ввели: '+text)
    entry.delete(0, 'end')

def clear_key(event):
    text=entry.get()
    label.config(text='Вы ввели: '+text)
    entry.delete(0, 'end')

def clear_all():
    text=entry.get()
    label.config(text='Вы ввели: ')
    entry.delete(0, 'end')

window=tk.Tk()

window.geometry('300x200')
window.title('Пример')

frame = tk.Frame(window, padx = 10, pady = 10)
frame.pack(expand=True)

entry=tk.Entry(frame)
entry.pack()
entry.bind('<Return>',clear_key)

button=tk.Button(frame, text='Очистить', command=clear)
button.pack()

label=tk.Label(frame, text='')
label.pack()

button2=tk.Button(frame, text='Очистить все', command=clear_all)
button2.pack()

button3=tk.Button(frame, text='Выход',command=lambda: window.destroy())
button3.pack()


window.mainloop()'''