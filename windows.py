from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
root.title('Python Coding')

global counter
counter = 1

def open():
    global counter

    if counter < 4:
        top = Toplevel()
        top.geometry("300x200")
        top.title('PAX')

        my_label = Label(top, text="NUEVA VENTANA", font=("Helvetica, 20"))
        my_label.pack(pady=50, padx=10)

        counter += 1
    else:
        messagebox.showinfo("Error", f"ya abriste {counter - 1} ventanas ")    

my_button = Button(root, text="Abrir Ventana", command=open)        
my_button.pack(pady=50, padx=50)

mainloop()

