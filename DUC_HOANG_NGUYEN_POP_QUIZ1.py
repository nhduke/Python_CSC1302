from tkinter import Tk, messagebox, LEFT, RIGHT, Label, Button

root = Tk()
root.title("My Info")
root.geometry("300x300")

def show_email():
    messagebox.showinfo("Email", "dnguyen241@students.gsu.edu")

last_name_label = Label(root, text="Nguyen")
first_name_label = Label(root, text="Duc Hoang")

last_name_label.pack(side=LEFT)
first_name_label.pack(side=RIGHT)

email_button = Button(root, text="Show Email", command=show_email)
email_button.pack(pady=20)

root.mainloop()
