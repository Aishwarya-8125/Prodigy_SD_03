import json
import os

FILE_NAME = "contacts.json"


# ---------------- LOAD DATA ----------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# ---------------- SAVE DATA ----------------
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- ADD CONTACT ----------------
def add_contact(contacts):
    print("\n➕ ADD NEW CONTACT")

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("✅ Contact Saved Successfully!")


# ---------------- VIEW CONTACTS ----------------
def view_contacts(contacts):
    print("\n📒 CONTACT LIST")

    if len(contacts) == 0:
        print("⚠ No contacts available")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


# ---------------- EDIT CONTACT ----------------
def edit_contact(contacts):
    print("\n✏ EDIT CONTACT")

    view_contacts(contacts)

    if len(contacts) == 0:
        return

    try:
        index = int(input("Enter contact number: ")) - 1

        if 0 <= index < len(contacts):
            print("Leave blank to keep old value")

            name = input("New Name: ")
            phone = input("New Phone: ")
            email = input("New Email: ")

            if name:
                contacts[index]["name"] = name
            if phone:
                contacts[index]["phone"] = phone
            if email:
                contacts[index]["email"] = email

            save_contacts(contacts)
            print("✅ Contact Updated Successfully!")

        else:
            print("❌ Invalid selection")

    except ValueError:
        print("❌ Enter valid number")


# ---------------- DELETE CONTACT ----------------
def delete_contact(contacts):
    print("\n🗑 DELETE CONTACT")

    view_contacts(contacts)

    if len(contacts) == 0:
        return

    try:
        index = int(input("Enter contact number: ")) - 1

        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"🗑 Deleted: {removed['name']}")
        else:
            print("❌ Invalid selection")

    except ValueError:
        print("❌ Enter valid number")


# ---------------- MAIN APP ----------------
def main():
    contacts = load_contacts()

    while True:
        print("\n==============================")
        print("📱 CONTACT MANAGEMENT APP")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("==============================")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            edit_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("\n👋 Exiting App... Goodbye!")
            break

        else:
            print("❌ Invalid option")


# RUN APP
if __name__ == "__main__":
    main()