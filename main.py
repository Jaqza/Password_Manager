from tkinter import *
from generate import Generator
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
generator = Generator()

def generate_password():
    pass_entry.delete(0,END)
    pass_entry.insert(0,string=generator.generate_new_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = web_entry.get()
    password = pass_entry.get()
    user_e_mail = e_mail.get()
    if len(website) == 0 or len(password) == 0 or len(user_e_mail) == 0 :
        messagebox.showwarning(message="Be sure to fill all fields")
    elif messagebox.askyesno(title="Do you want add content to data.txt ?",
                             message=f"\n\nWebsite:  {website}\nE-mail:  {user_e_mail}\nPassword:  {password}\nto a file ?"):
        with open("data.txt", "a") as file:
            file.write(f"{website} | {user_e_mail} | {password}\n")
            web_entry.delete(0,END)
            pass_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.configure(pady=50,padx=50)
window.minsize(width=240,height=240)

image = PhotoImage(file="../../Password_Manager/img.png")
canvas = Canvas()
canvas.configure(width=200,height=189)
canvas.create_image(100,94,image=image)
canvas.grid(column=3,row=0)

web_label = Label()
web_label.configure(text="Website :")
web_label.grid(column=0,row=1,sticky=W)

user = Label()
user.configure(text="E-mail/username :")
user.grid(column=0,row=2,sticky=W)

password_label = Label()
password_label.configure(text="Password :")
password_label.grid(column=0,row=3,sticky=W)

web_entry = Entry()
web_entry.configure(justify="center")
web_entry.focus()
web_entry.grid(column=3,row=1,columnspan=2,sticky=[W,E])

e_mail = Entry()
e_mail.configure(justify="center")
e_mail.insert(END,"afe@bananamail.com")
e_mail.grid(column=3,row=2,columnspan=2,sticky=[W,E])

pass_entry = Entry()
pass_entry.configure(width=20)
pass_entry.grid(column=3,row=3,sticky=[E,W])

password_button = Button()
password_button.configure(text="Generate Password",command=generate_password)
password_button.grid(column=4,row=3,sticky=E)

add_button = Button(command=add_to_file)
add_button.configure(text="Add",justify="center")
add_button.grid(column=2,columnspan=3,sticky=[E,W])






window.mainloop()