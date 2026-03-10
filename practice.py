import tkinter as tk
window = tk.Tk()

window.title("practice ")
window.geometry('400x400')

label_username = tk.Label (window,text="username",
font = ('timmes', 15, ),
fg= 'white',
bg='black'
)
label_username.pack()
entry =tk.Entry(window,width= 20)
entry.pack()

label_password= tk.Label(window, text="password",
font = ('times', 15, ),
fg= 'white',
bg ='black')
label_password.pack()

Entry = tk.Entry(window, width =20)
Entry.pack()

button= tk.Button(window, text='login ')
button.pack()

window.mainloop()

