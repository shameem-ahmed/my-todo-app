import streamlit as st
from functions import get_todos, write_todos

# streamlit run 013web.py

# pip freeze > requirements.txt

# http://share.streamlit.io/
# https://shameem-todo.streamlit.app/

todos = get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state['txtTodo']
    todos.append(f"{todo}\n")
    write_todos(newtodos=todos)


st.title('My TODOs')
st.subheader('This is my TODOs list.')
st.write('This is to increase my <b>productivity.</b>', unsafe_allow_html=True)

st.text_input(label='Enter a todo:', placeholder='Enter a new todo...', on_change=add_todo, key='txtTodo')

for i, todo in enumerate(todos):
    if todo != "\n":
        chk = st.checkbox(todo, False, i)
        if chk:
            todos.pop(i)
            write_todos(newtodos=todos)
            del st.session_state[i]
            st.rerun()


# st.session_state


