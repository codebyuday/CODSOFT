import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n" + "="*70)
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<20}")
    print("="*70)
    for contact in contacts:
        print(f"{contact['id']:<5} {contact['name']:<20} {contact['phone']:<15} {contact['email']:<20}")
    print("="*70)

def display_contact_detail(contact):
    print("\n" + "-"*40)
    print(f"Name:    {contact['name']}")
    print(f"Phone:   {contact['phone']}")
    print(f"Email:   {contact['email']}")
    print(f"Address: {contact['address']}")
    print("-"*40)

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Phone number cannot be empty.")
        return
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contact_id = max([c['id'] for c in contacts], default=0) + 1
    new_contact = {
        'id': contact_id,
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    print("\n--- Contact List ---")
    display_contacts(contacts)

def search_contacts(contacts):
    if not contacts:
        print("\nNo contacts to search.")
        return
    query = input("\nEnter name or phone to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print(f"\nFound {len(results)} contact(s):")
        display_contacts(results)
        show_detail = input("\nView full details? (y/n): ").strip().lower()
        if show_detail == 'y':
            for contact in results:
                display_contact_detail(contact)
    else:
        print("No contacts found matching your search.")

def update_contact(contacts):
    if not contacts:
        print("\nNo contacts to update.")
        return
    display_contacts(contacts)
    try:
        contact_id = int(input("\nEnter contact ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
    for contact in contacts:
        if contact['id'] == contact_id:
            print("\nCurrent details:")
            display_contact_detail(contact)
            print("\nEnter new details (press Enter to keep current):")
            name = input(f"Name [{contact['name']}]: ").strip()
            phone = input(f"Phone [{contact['phone']}]: ").strip()
            email = input(f"Email [{contact['email']}]: ").strip()
            address = input(f"Address [{contact['address']}]: ").strip()
            
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address
            
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    if not contacts:
        print("\nNo contacts to delete.")
        return
    display_contacts(contacts)
    try:
        contact_id = int(input("\nEnter contact ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    for i, contact in enumerate(contacts):
        if contact['id'] == contact_id:
            confirm = input(f"Delete '{contact['name']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                removed = contacts.pop(i)
                save_contacts(contacts)
                print(f"Contact '{removed['name']}' deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print("Contact not found.")

def show_statistics(contacts):
    total = len(contacts)
    with_email = sum(1 for c in contacts if c['email'])
    with_address = sum(1 for c in contacts if c['address'])
    print("\n--- Contact Statistics ---")
    print(f"Total contacts: {total}")
    print(f"With email: {with_email}")
    print(f"With address: {with_address}")

def main():
    contacts = load_contacts()
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Statistics")
        print("7. Exit")
        choice = input("\nEnter your choice (1-7): ").strip()
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            show_statistics(contacts)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
