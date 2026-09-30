import streamlit as st

st.title("📝 To-Do List")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Task input
task = st.text_input("Enter a new task")

# Add task
if st.button("Add Task"):
    if task.strip():
        st.session_state.tasks.append({
            "task": task,
            "completed": False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task.")

st.subheader("My Tasks")

# Display tasks
for i, item in enumerate(st.session_state.tasks):
    completed = st.checkbox(
        item["task"],
        value=item["completed"],
        key=f"task_{i}"
    )
    
    st.session_state.tasks[i]["completed"] = completed

# Delete completed tasks
if st.button("Delete Completed Tasks"):
    st.session_state.tasks = [
        item for item in st.session_state.tasks
        if not item["completed"]
    ]
    st.rerun()

# Clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.rerun()