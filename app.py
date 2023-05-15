import streamlit as st
import os
# from dotenv import load_dotenv
import streamlit_google_oauth as oauth

# load_dotenv()
client_id = "657069732284-mbcb1l7ra4pask18n2cc7a29123ldsm3.apps.googleusercontent.com"
client_secret = "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"
redirect_uri = "http://localhost:8501"


if __name__ == "__main__":
    app_name = '''
    Streamlit Google Authentication Demo
    '''
    app_desc = '''
    A streamlit application that authenticates users by <strong>Google Oauth</strong>.
    The user must have a google account to log in into the application.
    '''
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        app_name=app_name,
        app_desc=app_desc,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        st.write(f"Welcome {user_email}")
        # st.write(login_info)

# streamlit run app.py --server.port 8501
