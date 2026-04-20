import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


contacts = load_contacts()


def refresh_list():
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} | {c['phone']} | {c['email']}")


def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()

    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error", "All fields required")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    refresh_list()

    name_var.set("")
    phone_var.set("")
    email_var.set("")


def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select contact")
        return

    contacts.pop(selected[0])
    save_contacts(contacts)
    refresh_list()


# WINDOW
root = tk.Tk()
root.title("Contact Manager App")
root.geometry("500x400")


# INPUT FIELDS
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Phone").pack()
tk.Entry(root, textvariable=phone_var).pack()

tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack()


# BUTTONS
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_contact).pack(pady=5)


# LISTBOX
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

refresh_list()

root.mainloop()