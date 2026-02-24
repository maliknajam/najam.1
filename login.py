import tkinter as tk
window = tk.Tk()

window.title("login page")
window.geometry("500x500")

def login():
    if (label_username_entry.get() == 'najam') & (label_password_entry.get() == '123'):
        label_message.configure(text='login successful' ,fg='green')
    else:
        label_message.configure(text='login unsuccessful' , fg='red')
label_username = tk.Label(window,text="username")
label_username_entry = tk.Entry(window, width=50)
label_username.pack()
label_username_entry.pack()


label_password = tk.Label(window,text="password")
label_password_entry = tk.Entry(window, width=50)
label_password.pack()
label_password_entry.pack()



button = tk.Button(window,text="login",command=login)
button.pack()
label_message = tk.Label(window,text="")
label_message.pack()

window.mainloop()