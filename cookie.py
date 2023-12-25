import streamlit as st
from google.auth.transport.requests import Request
from google.oauth2 import id_token

CLIENT_ID = 'your_google_client_id'  # Replace with your Google Client ID


def login_with_google():
    st.title('Google Login with Streamlit')

    st.sidebar.header('User Authentication')

    if 'google_token' not in st.session_state:
        st.session_state.google_token = st.text_input('Enter Google ID Token:')
        st.session_state.user_info = None
        st.session_state.login_error = None

        if st.button('Login'):
            id_info = verify_google_token(st.session_state.google_token)
            if id_info:
                st.session_state.user_info = id_info
            else:
                st.session_state.login_error = 'Invalid Google ID Token. Please try again.'

    else:
        st.session_state.user_info = None
        st.session_state.login_error = None

        if st.button('Logout'):
            st.session_state.google_token = None

    if st.session_state.user_info:
        st.success(f'Login successful! Welcome, {st.session_state.user_info["name"]}!')

    if st.session_state.login_error:
        st.error(st.session_state.login_error)


def verify_google_token(token):
    try:
        id_info = id_token.verify_oauth2_token(token, Request(), CLIENT_ID)
        return id_info
    except ValueError as e:
        st.error(f'Error verifying Google ID Token: {e}')
        return None


if __name__ == '__main__':
    login_with_google()
