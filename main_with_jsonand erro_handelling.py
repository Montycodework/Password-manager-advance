from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ["!","#","$","%","&","*","(",")","+"]
    from random import choice, randint, shuffle
    password_letter = [choice(alphabets) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letter+password_number+password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- # step 2
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data ={
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="All fields are mandatory to fill")
    else:
        try:
            with open('data.json','r') as file:
                read_data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            read_data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(read_data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- # step 1
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="Data file not exists!")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n Password: {password}')
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- # step 1
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
mypass_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=mypass_img)
canvas.grid(row=0, column=1)


website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)


website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# After handelling the errors we are adding a search feature
# so add the search button first

search = Button(text="Search", command=find_password)
search.grid(row=1, column=2)


generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2, columnspan=2)
Add_button = Button(text="Add", width=36, command=save_password)
Add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
