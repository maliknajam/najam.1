import tkinter as tk

window = tk.Tk()
window.title("my first GUI")
window.geometry("400x300")

label_username = tk.Label(
    window,
    text="User name",
    font=("times new roman", 20),
    fg="white",
    bg="black"
)
label_username.pack()

entry = tk.Entry(window, width=50)
entry.pack()

click_count = 0

def take():
    global click_count
    data = entry.get()
    print("data :", data)

    click_count += 1

    if click_count % 2 == 1:
        button.config(bg="green")
    else:
        button.config(bg="red")


button = tk.Button(window, text="click", command=take)
button.pack()

window.mainloop()