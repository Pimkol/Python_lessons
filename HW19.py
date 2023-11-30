import tkinter as tk

#1
'''
window=tk.Tk()
window.title('Выход')
window.geometry('250x100')

frame = tk.Frame(window, padx = 10, pady = 10)
frame.pack(expand=True)

button=tk.Button(frame, text='Выход',command=lambda: window.destroy())
button.pack()

window.mainloop()'''

#2
'''
window=tk.Tk()
window.title('Анкета')
window.geometry('350x250')

frame = tk.Frame(window, padx = 10, pady = 10)
frame.pack(expand=True)

label=tk.Label(frame, text='Имя: Ольга \nВозраст: 29 лет.\nМесто работы: бухгалтерия')
label.pack()

window.mainloop()'''