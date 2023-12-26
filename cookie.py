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

    # Load data from the JSON file
    data = load_data()

    # Display current data
    st.subheader("Current Data:")
    st.write(data)

    # Input new key-value pair
    user_name = st.text_input("Enter username")
    password = st.text_input("Enter password")

    # Add the new key-value pair to the data
    if st.button("Add to Dictionary"):
        if key and value:
            if user_name not in data:
                data[key] = value
                st.success(f"Added: {user_name}: {password}")
                save_data(data)
            else:
                st.write("this username is taken")
        else:
            st.warning("Please enter both key and value.")

    # Display updated data
    st.subheader("Updated Data:")
    st.write(data)

    # Clear data button
    if st.button("Clear Data"):
        data.clear()
        st.warning("All data cleared.")
        save_data(data)

if __name__ == "__main__":
    main()
