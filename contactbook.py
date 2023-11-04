import os
import json

def load():
    if os.path.exists('mob_nums.json'):
        with open('mob_nums.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save(mob_nums):
    with open('mob_nums.json', 'w') as file:
        json.dump(mob_nums, file, indent=4)

def add():
    name = input("Enter the person name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the person email: ")

    new = {
        'name': name,
        'phone': phone,
        'email': email
    }

    mob_nums = load()
    mob_nums.append(new)
    save(mob_nums)
    print(f"Contact {name} added successfully")

def lists():
    mob_nums = load()
    if mob_nums:
        print("\nContacts:")
        for index, contact in enumerate(mob_nums, start=1):
            print(f"{index}. {contact['name']} - Phone: {contact['phone']} - Email: {contact['email']}")
    else:
        print("The phone book is empty.")

def search():
    name_to_search = input("Enter the name to search for: ")
    mob_nums = load()
    found = False

    for contact in mob_nums:
        if name_to_search.lower() in contact['name'].lower():
            print(f"Contact found:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
            found = True

    if not found:
        print(f"No contact found with the name '{name_to_search}'.")

while True:
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. List all mob_nums")
    print("3. Search for a contact by name")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add()
    elif choice == '2':
        lists()
    elif choice == '3':
        search()
    elif choice == '4':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please enter valid choice(1/2/3/4).")
