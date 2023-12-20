import tkinter as tk


'''def on_checkbox():
    if var.get()==1:
        rez_label.config(text='bu')
    else:
        rez_label.config(text='b4u')'''

def show_state():
    rez_label.config(text=f'опция 1:{var1.get()}, Опция2: {var2.get()}')

root=tk.Tk()
root.title('hw')

var1=tk.IntVar()
var2=tk.IntVar()

checkbutt1=tk.Checkbutton(root, text='dfgd',variable=var1, onvalue=1, offvalue=2)#command=on_checkbox)
checkbutt2=tk.Checkbutton(root, text='dfgd',variable=var2, onvalue=1, offvalue=2)#command=on_checkbox)
checkbutt1.pack()
checkbutt2.pack()

show_button=tk.Button(root, text='cостояние', command=show_state)
show_button.pack()

rez_label=tk.Label(root, text='')
rez_label.pack()

root.mainloop()
#какое обучение, такое и дз
# Для корректного выполнения д/з буду рад вас видеть на занятиях на которых идет полный разбор методов. 
# Так же готов лично выслушать претензии, вы всегда можете созвонится со мной в личном порядке в удобное для вас и меня время
