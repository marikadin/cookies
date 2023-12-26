import streamlit as st
import json

# Function to read the JSON file
def load_data():
    try:
        with open("secrets.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

# Function to save data to the JSON file
def save_data(data):
    with open("secrets.json", "w") as f:
        json.dump(data, f, indent=2)

# Streamlit app
def main():
    st.title("Streamlit JSON Editor")
    page = st.sidebar.radio("Select Page", ["login", "sign up"])

    if page == "login":
        login()
    elif page == "sign up":
        sign_up()

def sign_up():
    # Load data from the JSON file
    data = load_data()

    # Display current data
    st.subheader("Current Data:")
    st.write(data)

    user_name = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")

    # Check if the username already exists in the dictionary
    if user_name in data:
        st.warning("Username already exists. Please choose a different username.")
        # Clear the password input field when the username is taken
        password = ""
    else:
        # Add the new key-value pair to the data
        if st.button("Add to Dictionary"):
            if user_name and password:
                data[user_name] = password
                st.success(f"Added: {user_name}: {password}")
                save_data(data)
                # Clear input fields after successfully adding data
                user_name = ""
                password = ""
            else:
                st.warning("Please enter both username and password.")

    # Display updated data
    st.subheader("Updated Data:")
    st.write(data)

    # Clear data button
    if st.button("Clear Data"):
        data.clear()
        st.warning("All data cleared.")
        save_data(data)

def login():
    # Load data from the JSON file
    data = load_data()

    # Display current data
    st.subheader("Current Data:")
    st.write(data)

    login_user_name = st.text_input("Enter username for login")
    login_password = st.text_input("Enter password for login", type="password")

    # Check if the entered username and password match
    if login_user_name in data and data[login_user_name] == login_password:
        st.success(f"Login successful for user: {login_user_name}")

        # Add a Logout button
        if st.button("Logout"):
            st.info("Logged out successfully.")
    else:
        st.warning("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
