import pyperclip as pc
from random import choice, randint, shuffle
from tkinter import Button, Canvas, END, Entry, Label, messagebox, PhotoImage, Tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    if len(password_entry.get()) > 0:
        password_entry.delete(first=0, last=END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(index=0, string=password)
    pc.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Validation Error", message="Please fill all fields")
    else:
        with open(file="data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")

    website_entry.delete(first=0, last=END)
    password_entry.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")

window.title("Password Manager")
window.config(padx=50, pady=50)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="W")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="W")

# Input Boxes
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(index=0, string="firasnaber@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate)
generate_password_button.grid(row=3, column=2)
add_password_button = Button(text="Add", width=35, command=save)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
