import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"


# ---------------- DATA HANDLING ----------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


contacts = load_contacts()


# ---------------- UI FUNCTIONS ----------------
def refresh_list(data=None):
    listbox.delete(0, tk.END)
    show_data = data if data is not None else contacts

    for c in show_data:
        listbox.insert(tk.END, f"{c['name']} | {c['phone']} | {c['email']}")


def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()

    if not name or not phone or not email:
        messagebox.showerror("Error", "All fields are required")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()

    refresh_list()

    name_var.set("")
    phone_var.set("")
    email_var.set("")

    messagebox.showinfo("Success", "Contact Added Successfully!")


def delete_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact")
        return

    contacts.pop(selected[0])
    save_contacts()
    refresh_list()


def search_contact():
    query = search_var.get().lower()

    filtered = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"]
    ]

    refresh_list(filtered)


def reset_search():
    search_var.set("")
    refresh_list()


# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Smart Contact Manager")
root.geometry("650x500")
root.config(bg="#1e1e2f")


# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="📒 Smart Contact Manager",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=10)


# ---------------- INPUT FRAME ----------------
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(frame, text="Name", fg="white", bg="#1e1e2f").grid(row=0, column=0)
tk.Entry(frame, textvariable=name_var, width=25).grid(row=0, column=1)

tk.Label(frame, text="Phone", fg="white", bg="#1e1e2f").grid(row=1, column=0)
tk.Entry(frame, textvariable=phone_var, width=25).grid(row=1, column=1)

tk.Label(frame, text="Email", fg="white", bg="#1e1e2f").grid(row=2, column=0)
tk.Entry(frame, textvariable=email_var, width=25).grid(row=2, column=1)


# ---------------- BUTTONS ----------------
tk.Button(root, text="➕ Add Contact", bg="green", fg="white", command=add_contact).pack(pady=5)
tk.Button(root, text="🗑 Delete Contact", bg="red", fg="white", command=delete_contact).pack(pady=5)


# ---------------- SEARCH ----------------
search_var = tk.StringVar()

search_frame = tk.Frame(root, bg="#1e1e2f")
search_frame.pack(pady=10)

tk.Entry(search_frame, textvariable=search_var, width=30).grid(row=0, column=0)
tk.Button(search_frame, text="🔍 Search", command=search_contact).grid(row=0, column=1)
tk.Button(search_frame, text="Reset", command=reset_search).grid(row=0, column=2)


# ---------------- LISTBOX ----------------
listbox = tk.Listbox(root, width=70, height=12)
listbox.pack(pady=10)

refresh_list()


root.mainloop()