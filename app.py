from orchestrator import run_analysis
from search_bug import search_similar_bugs
import os
import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Smart Bug Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("🤖 AI Smart Bug Analyzer")
st.sidebar.write("### Project Information")
st.sidebar.success("Milestone 2 Completed ✅")
st.sidebar.info("Model : all-MiniLM-L6-v2")
st.sidebar.info("Database : FAISS")
st.sidebar.info("Framework : Streamlit")

# ---------------- Title ----------------
st.title("🐞 AI Smart Bug Analyzer & Fix Advisor")
st.write("Submit a bug report to analyze severity, logs, and retrieve similar historical bugs.")

# ---------------- Inputs ----------------
bug_title = st.text_input("Bug Title")
bug_description = st.text_area("Bug Description")
error_log = st.text_area("Error Log / Stack Trace")

uploaded_file = st.file_uploader(
    "Upload Bug Report / Error Log",
    type=["txt", "log", "pdf"]
)

# ---------------- Submit ----------------
if st.button("🚀 Submit Bug"):

    st.success("✅ Bug Submitted Successfully!")

    # Save uploaded file
    if uploaded_file is not None:

        os.makedirs("uploads", exist_ok=True)

        save_path = os.path.join("uploads", uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"📄 File '{uploaded_file.name}' uploaded successfully!")

    # Submitted Details
    st.divider()

    st.subheader("📋 Submitted Bug Details")

    st.write("**🐞 Bug Title:**", bug_title)
    st.write("**📝 Bug Description:**", bug_description)
    st.write("**⚠ Error Log:**", error_log)

    if uploaded_file is not None:
        st.write("**📎 Uploaded File:**", uploaded_file.name)

    else:
        st.write("No file uploaded.")

    # ---------------- Processing ----------------

    with st.spinner("🔍 Analyzing Bug..."):

        analysis = run_analysis(bug_description, error_log)

    st.divider()

    # ---------------- TRIAGE ----------------

    st.subheader("🤖 Triage Agent")

    triage = analysis["Triage Agent"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔥 Severity", triage["Severity"])

    with col2:
        st.metric("⚡ Priority", triage["Priority"])

    with col3:
        st.metric("🎯 Confidence", f"{triage['Confidence']}%")

    st.info(f"🧩 Component : {triage['Component']}")

    with st.expander("💡 Reasoning"):
        st.write(triage["Reasoning"])

    st.divider()

    # ---------------- LOG ANALYSIS ----------------

    st.subheader("📄 Log Analysis")

    log = analysis["Log Analysis Agent"]

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"**Exception**\n\n{log['Exception']}")

    with col2:
        st.warning(f"**Failure Point**\n\n{log['Failure Point']}")

    st.info(f"📍 Affected Code Path : {log['Affected Code Path']}")

    st.divider()

    # ---------------- Similar Bugs ----------------

    st.subheader("🔍 Top Similar Bugs")

    results = search_similar_bugs(bug_description)

    for i, bug in enumerate(results):

        with st.expander(f"🐞 Similar Bug {i+1}"):

            st.write(bug)