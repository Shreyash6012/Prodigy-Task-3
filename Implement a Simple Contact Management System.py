import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

contacts = load_contacts()

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts()
    update_listbox()
    clear_entries()
    messagebox.showinfo("Success", "Contact added successfully!")

def update_listbox():
    listbox.delete(0, tk.END)
    for name in contacts:
        listbox.insert(tk.END, name)

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def select_contact(event):
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)

        entry_name.insert(0, name)
        entry_phone.insert(0, contacts[name]["Phone"])
        entry_email.insert(0, contacts[name]["Email"])

def update_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name in contacts:
        contacts[name] = {"Phone": phone, "Email": email}
        save_contacts()
        update_listbox()
        messagebox.showinfo("Updated", "Contact updated successfully!")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected)
        del contacts[name]
        save_contacts()
        update_listbox()
        clear_entries()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")

# GUI Window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("420x420")
root.resizable(False, False)

# Labels & Entries
tk.Label(root, text="Contact Management System", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame)
entry_phone.grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame)
entry_email.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add Contact", width=15, command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", width=15, command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=15, command=delete_contact).pack(pady=5)

# Contact List
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", select_contact)

update_listbox()
root.mainloop()
