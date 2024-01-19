import sqlite3

# Create a SQLite database and table
def create_table():
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            phone_number TEXT,
            email TEXT
        )
    ''')
    connection.commit()
    connection.close()

# Function to add a new contact
def add_contact(name, address, phone_number, email):
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, address, phone_number, email)
        VALUES (?, ?, ?, ?)
    ''', (name, address, phone_number, email))
    connection.commit()
    connection.close()
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()
    cursor.execute('''
        SELECT * FROM contacts
    ''')
    contacts = cursor.fetchall()
    connection.close()

    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print("ID:", contact[0])
            print("Name:", contact[1])
            print("Address:", contact[2])
            print("Phone Number:", contact[3])
            print("Email:", contact[4])
            print("-" * 20)

# Function to update a contact
def update_contact(contact_id, name, address, phone_number, email):
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE contacts
        SET name=?, address=?, phone_number=?, email=?
        WHERE id=?
    ''', (name, address, phone_number, email, contact_id))
    connection.commit()
    connection.close()
    print("Contact updated successfully!")

# Function to delete a contact
def delete_contact(contact_id):
    connection = sqlite3.connect("contact_book.db")
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM contacts WHERE id=?
    ''', (contact_id,))
    connection.commit()
    connection.close()
    print("Contact deleted successfully!")

# Main function
def main():
    create_table()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            add_contact(name, address, phone_number, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            contact_id = int(input("Enter Contact ID to update: "))
            name = input("Enter New Name: ")
            address = input("Enter New Address: ")
            phone_number = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            update_contact(contact_id, name, address, phone_number, email)

        elif choice == '4':
            contact_id = int(input("Enter Contact ID to delete: "))
            delete_contact(contact_id)

        elif choice == '5':
            print('Exiting contact Book. Goodbye')
            break
        else:
            print('invalid choice. Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()
