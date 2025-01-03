from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip # type: ignore
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    #print(f"Your password is: {password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", mode="a+") as file:
                file.write(f"\n{website} | {email} | {password}")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,  pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font="Courier")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font="Courier")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font="Courier")
password_label.grid(column=0, row=3)

website_input = Entry(width=30)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=48)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "myemail@yahoo.com")

password_input = Entry(width=30)
password_input.grid(column=1, row=3)

search_button = Button(text="Search", width=14) #, command=find_password)
search_button.grid(column=2, row=1)

genpass_button = Button(text="Generate Password", width=14, command=generate_password)
genpass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()