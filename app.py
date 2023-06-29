import streamlit as st
import requests as r

def main():
    query = st.text_input("Enter the email:")
    if query:
        results = r.get(f"https://lambda-functions-v2.api.level.game/v1/clevertap/user-management?email={query}")
        if(results.status_code == 200):
            st.text("User unsubscribed")

if __name__ == '__main__':
    main()
