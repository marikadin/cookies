import streamlit as st
import json

# Function to read the JSON file
def load_data():
    try:
        with open("secrets.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
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
    key = st.text_input("Enter Key:")
    value = st.text_input("Enter Value:")

    # Add the new key-value pair to the data
    if st.button("Add to Dictionary"):
        if key and value:
            data[key] = value
            st.success(f"Added: {key}: {value}")
            save_data(data)
        else:
            st.warning("Please enter both key and value.")

    # Display updated data
    st.subheader("Updated Data:")
    st.write(data)

    # Save data to the JSON file before exiting
    save_data(data)

if __name__ == "__main__":
    main()
