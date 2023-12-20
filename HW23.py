import tkinter as tk
from tkinter import ttk

def show_selection():
    sel_value.set(combobox.get())
    selected_items = listbox.curselection()
    selected_values = [listbox.get(i) for i in selected_items]
    label.config(text=f"Чтобы приготовить {sel_value.get()} \n Вам понадобиться:\n {', '.join(selected_values)}")
#Если верно понял суть программы, то испраавил добавив вызов get() для sel_value в методе show_selection().


window = tk.Tk()
window.title('Генератор рецептов')
window.geometry('350x350')

frame = tk.Frame(window, padx=10, pady=10)
frame.pack(expand=True)

value11s = ['суп', 'основное блюдо', 'салат']

sel_value = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=sel_value, values=value11s)
combobox.pack()

x = combobox.get()

listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE)
listbox.pack()

for item in ['помидоры', 'огурцы', 'яйца', 'курица', 'сыр', 'карфель', 'лук', 'грибы', 'зелень']:
    listbox.insert(tk.END, item)

button = tk.Button(frame, text='Показать ингредиенты', command=show_selection)
button.pack()

label = tk.Label(frame, text='')
label.pack()

window.mainloop()
