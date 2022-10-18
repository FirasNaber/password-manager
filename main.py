import json
import pyperclip as pc
from random import choice, randint, shuffle
from tkinter import Button, Canvas, END, Entry, Label, messagebox, PhotoImage, Tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    if len(password_entry.get()) > 0:
        password_entry.delete(first=0, last=END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
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

# ---------------------------- SEARCH WEBSITE ------------------------------ #


def search():
    website = website_entry.get().lower()

    try:
        with open(file="data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")
    else:
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website.title()} Login Information", message=f"Email: {email}"
                                                                                      f"\nPassword: {password}")
        elif website == "":
            messagebox.showerror(title="Error", message="Please enter a website to search for.")
        else:
            messagebox.showerror(title="Error", message=f"No login information for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website.lower(): {
            "email": email.lower(),
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Validation Error", message="Please fill all fields.")
    else:
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        with open('data.json', mode='w') as data_file:
            json.dump(data, data_file, indent=4)


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
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(index=0, string="firasnaber@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")
generate_password_button = Button(text="Generate Password", command=generate)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_password_button = Button(text="Add", width=35, command=add)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
