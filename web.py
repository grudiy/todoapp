import streamlit as st

import functions

todos = functions.get_todos()

st.title("My ToDo App")
st.subheader("This is my ToDo list")
st.write("This app can increase your productivity")

i = 1
for todo in todos:
    st.checkbox(todo, key=f"todo-{i}")
    i = i + 1

st.text_input(label="Add ToDo", placeholder="Enter a new ToDo")
