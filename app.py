from search_bug import search_similar_bugs
import os
import streamlit as st

st.title("AI Smart Bug Analyzer & Fix Advisor")
st.write("Welcome to the Bug Submission Module")

bug_title = st.text_input("Bug Title")

bug_description = st.text_area("Bug Description")

error_log = st.text_area("Error Log / Stack Trace")

uploaded_file = st.file_uploader(
    "Upload Bug Report / Error Log",
    type=["txt", "log", "pdf"]
)

if st.button("Submit"):
    st.success("Bug Submitted Successfully!")

    if uploaded_file is not None:
        save_path = os.path.join("uploads", uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    st.subheader("Submitted Bug Details")
    st.write("**Bug Title:**", bug_title)
    st.write("**Bug Description:**", bug_description)
    st.write("**Error Log / Stack Trace:**", error_log)
    st.subheader("Top Similar Bugs")

results = search_similar_bugs(bug_description)

for i, bug in enumerate(results):
    st.write(f"### Bug {i+1}")
    st.write(bug)
    st.write("---")

    if uploaded_file is not None:
        st.write("**Uploaded File:**", uploaded_file.name)
    else:
        st.write("No file uploaded.")