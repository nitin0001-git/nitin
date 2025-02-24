import streamlit as st
import sqlite3

def create_connection():
    return sqlite3.connect("contacts.db")

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def add_contact(name, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

def view_contacts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    conn.close()
    return data

def delete_contact(contact_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

def main():
    st.title("Contact Management System")
    
    menu = ["Add Contact", "View Contacts", "Delete Contact"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    create_table()
    
    if choice == "Add Contact":
        st.subheader("Add a New Contact")
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        
        if st.button("Add Contact"):
            add_contact(name, email, phone)
            st.success(f"Contact {name} added successfully!")
    
    elif choice == "View Contacts":
        st.subheader("Contact List")
        contacts = view_contacts()
        for contact in contacts:
            st.write(f"ID: {contact[0]}, Name: {contact[1]}, Email: {contact[2]}, Phone: {contact[3]}")
    
    elif choice == "Delete Contact":
        st.subheader("Delete a Contact")
        contact_id = st.number_input("Enter Contact ID to Delete", min_value=1, step=1)
        
        if st.button("Delete Contact"):
            delete_contact(contact_id)
            st.success(f"Contact with ID {contact_id} deleted successfully!")

if __name__ == "__main__":
    main()