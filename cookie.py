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
            id_token_string = exchange_code_for_id_token(code)
            if id_token_string:
                user_info = authenticate_with_google(id_token_string)
                if user_info:
                    st.success(f"Successfully logged in as {user_info['name']} ({user_info['email']})")

                    # Save the user's email in Streamlit secrets
                    st.secrets["user_email"] = user_info['email']

                    # Display user information
                    st.write("User Information:")
                    st.write(f"Name: {user_info['name']}")
                    st.write(f"Email: {user_info['email']}")
                    st.write(f"User ID: {user_info['sub']}")
