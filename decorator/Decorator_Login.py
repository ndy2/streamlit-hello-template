from functools import wraps

import streamlit as st

from config.MyAuthenticate import ai_api_authenticate


def login_required(func):
    @wraps(func)
    def wrapper():
        st.set_page_config(
            initial_sidebar_state="collapsed"
        )
        name, authentication_status, username = ai_api_authenticate.login("로그인", "main")
        if authentication_status:
            ai_api_authenticate.logout('Logout', 'main', key='unique_key')
            func()
        elif authentication_status is False:
            st.error('Username/password is incorrect')
        elif authentication_status is None:
            st.warning('Please enter your username and password')

    return wrapper


@login_required
def hello():
    print('hello')


@login_required
def world():
    print('world')


if __name__ == "__main__":
    hello()
    world()
