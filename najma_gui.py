import tkinter as tk
window = tk.Tk()
window.title("my first GUI")
window.geometry("400x300")


label_username =tk.Label(window,text="User name" ,font=("times new roman", 20) ,fg="white" , bg="black")
label_username.pack()




def button_clicked():
    print("clicked")



def take ():
    input =entry.get()
    print ( "data : ", input )
entry  = tk.Entry(window, width = 50)
entry.pack()

button = tk.Button(window,text="click ",command=take)
button.pack()


window.mainloop()

