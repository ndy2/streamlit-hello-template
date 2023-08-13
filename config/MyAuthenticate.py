import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
ai_api_authenticate = stauth.Authenticate(
    {
        "usernames": {
            "jsmith": {
                "email": "jsmith@gmail.com",
                "name": "John Smith",
                "password": hashed_passwords[0]
            },
            "rbriggs": {
                "email": "rbriggs@gmail.com",
                "name": "Rebecca Briggs",
                "password": hashed_passwords[1]
            }
        }
    },
    "some_cookie_name",
    "some_signature_key",
    30,
    None,
    None
)
