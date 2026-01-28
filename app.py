import streamlit as st
from support_agent import resolve_ticket

st.title("AI Customer Support Agent")

ticket = st.text_area("Enter customer issue")

if st.button("Resolve"):
    category, response = resolve_ticket(ticket)
    st.success(f"Category: {category}")
    st.write(response)
