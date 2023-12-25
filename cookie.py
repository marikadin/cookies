import streamlit as st
from google.auth.transport.requests import Request
from google.oauth2 import id_token

# Set your Google OAuth client ID
CLIENT_ID = '250605044176-fqtehiqadj8deci2a2pmrs84k9c0kbv6.apps.googleusercontent.com'


def authenticate_with_google(id_token_string):
    try:
        # Verify the ID token using the Google Auth library
        id_info = id_token.verify_oauth2_token(id_token_string, Request(), CLIENT_ID)
        return id_info
    except Exception as e:
        st.error(f"Authentication failed: {e}")
        return None


def exchange_code_for_id_token_on_server(code):
    return get_actual_id_token_from_server(code)


if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


def main():
    st.title("Google Login with Streamlit")

    # Add a button to initiate the login process
    st.button('Analyze', on_click=click_button)
    if st.session_state.clicked:
        # Display a Google Sign-In button, allowing the user to sign in with their Google account
        login_url = f'https://accounts.google.com/o/oauth2/auth?client_id={CLIENT_ID}&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=openid%20profile%20email&response_type=code'
        st.markdown(f"[Sign in with Google]({login_url})")

        # After the user signs in, they will be redirected to a page with a code
        # Retrieve the code from the user input
        code = st.text_input("Enter the code from the redirected URL:")

        # Exchange the code for an ID token
        if code:
            id_token_string = exchange_code_for_id_token_on_server(code)
            if id_token_string:
                user_info = authenticate_with_google(id_token_string)
                if user_info:
                    st.success(f"Successfully logged in as {user_info['name']} ({user_info['email']})")

                    # Save the user's information in Streamlit secrets
                    st.secrets["user_info"] = user_info

                    # Display user information
                    st.write("User Information:")
                    st.write(f"Name: {user_info['name']}")
                    st.write(f"Email: {user_info['email']}")
                    st.write(f"User ID: {user_info['sub']}")


if __name__ == "__main__":
    main()
