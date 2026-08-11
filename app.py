from orchestrator import run_analysis
from search_bug import search_similar_bugs
from defect_analytics import analyze_defect_patterns
from knowledge_base_growth import add_resolved_bug
from testing_validation import validate_bug_history

import os
import json
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Intelligent Bug Diagnosis Platform",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "bug_title" not in st.session_state:
    st.session_state.bug_title = ""

if "bug_description" not in st.session_state:
    st.session_state.bug_description = ""

if "error_log" not in st.session_state:
    st.session_state.error_log = ""

if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None

if "knowledge_base_added" not in st.session_state:
    st.session_state.knowledge_base_added = False


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🤖 Intelligent Bug Diagnosis Platform")

st.sidebar.write("### Project Information")

st.sidebar.success("Milestone 4 Completed ✅")

st.sidebar.info("Model : all-MiniLM-L6-v2")
st.sidebar.info("Database : FAISS")
st.sidebar.info("Framework : Streamlit")
st.sidebar.info("LLM : Google Gemini")


# =========================================================
# TITLE
# =========================================================

st.title(
    "🐞 Creation of Intelligent Bug Diagnosis Platform "
    "with Fix Recommendation Assistance"
)

st.subheader("Group 2")

st.write(
    "An intelligent platform for automated bug diagnosis, "
    "root cause analysis, duplicate detection and fix recommendation."
)


# =========================================================
# INPUTS
# =========================================================

bug_title = st.text_input(
    "Bug Title",
    value=st.session_state.bug_title
)

bug_description = st.text_area(
    "Bug Description",
    value=st.session_state.bug_description
)

error_log = st.text_area(
    "Error Log / Stack Trace",
    value=st.session_state.error_log
)

uploaded_file = st.file_uploader(
    "Upload Bug Report / Error Log",
    type=["txt", "log", "pdf"]
)


# =========================================================
# SUBMIT BUG
# =========================================================

if st.button("🚀 Submit Bug"):

    # Reset previous knowledge-base confirmation
    st.session_state.knowledge_base_added = False

    # Save input values
    st.session_state.bug_title = bug_title
    st.session_state.bug_description = bug_description
    st.session_state.error_log = error_log

    if uploaded_file is not None:
        st.session_state.uploaded_file_name = uploaded_file.name
    else:
        st.session_state.uploaded_file_name = None

    st.success("✅ Bug Submitted Successfully!")


    # =====================================================
    # SAVE UPLOADED FILE
    # =====================================================

    if uploaded_file is not None:

        os.makedirs("uploads", exist_ok=True)

        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(
            f"📄 File '{uploaded_file.name}' uploaded successfully!"
        )


    # =====================================================
    # PROCESSING
    # =====================================================

    with st.spinner("🔍 Analyzing Bug..."):

        analysis = run_analysis(
            bug_description,
            error_log
        )

    # Store analysis in session
    st.session_state.analysis = analysis


    # =====================================================
    # SAVE BUG TO HISTORY
    # =====================================================

    os.makedirs("outputs", exist_ok=True)

    history_file = "outputs/bug_history.json"

    bug_record = {
        "Title": bug_title,
        "Description": bug_description,

        "Severity":
            analysis["Triage Agent"]["Severity"],

        "Priority":
            analysis["Triage Agent"]["Priority"],

        "Component":
            analysis["Triage Agent"]["Component"],

        "Exception":
            analysis["Log Analysis Agent"]["Exception"],

        "Failure Point":
            analysis["Log Analysis Agent"]["Failure Point"],

        "Root Cause":
            analysis["Root Cause Agent"]["Root Cause"]
    }


    if os.path.exists(history_file):

        try:

            with open(history_file, "r") as f:
                bug_history = json.load(f)

        except Exception:

            bug_history = []

    else:

        bug_history = []


    bug_history.append(bug_record)


    with open(history_file, "w") as f:

        json.dump(
            bug_history,
            f,
            indent=4
        )


# =========================================================
# SHOW ANALYSIS
# =========================================================

if st.session_state.analysis is not None:

    analysis = st.session_state.analysis

    bug_title = st.session_state.bug_title
    bug_description = st.session_state.bug_description
    error_log = st.session_state.error_log


    # =====================================================
    # SUBMITTED BUG DETAILS
    # =====================================================

    st.divider()

    st.subheader("📋 Submitted Bug Details")

    st.write(
        "**🐞 Bug Title:**",
        bug_title
    )

    st.write(
        "**📝 Bug Description:**",
        bug_description
    )

    st.write(
        "**⚠ Error Log:**",
        error_log
    )

    if st.session_state.uploaded_file_name is not None:

        st.write(
            "**📎 Uploaded File:**",
            st.session_state.uploaded_file_name
        )

    else:

        st.write("No file uploaded.")


    # =====================================================
    # TRIAGE AGENT
    # =====================================================

    st.divider()

    st.subheader("🤖 Triage Agent")

    triage = analysis["Triage Agent"]

    col1, col2, col3 = st.columns(3)


    with col1:

        severity = triage["Severity"]

        if severity == "High":

            st.error(
                f"🔥 Severity\n\n{severity}"
            )

        elif severity == "Medium":

            st.warning(
                f"🟡 Severity\n\n{severity}"
            )

        else:

            st.success(
                f"🟢 Severity\n\n{severity}"
            )


    with col2:

        st.metric(
            "⚡ Priority",
            triage["Priority"]
        )


    with col3:

        st.metric(
            "🎯 Confidence",
            f"{triage['Confidence']}%"
        )

        st.progress(
            triage["Confidence"] / 100
        )


    st.info(
        f"🧩 Component : {triage['Component']}"
    )


    with st.expander("💡 AI Reasoning"):

        st.write(
            triage["Reasoning"]
        )


    # =====================================================
    # LOG ANALYSIS AGENT
    # =====================================================

    st.divider()

    st.subheader("📄 Log Analysis")

    log = analysis["Log Analysis Agent"]

    col1, col2 = st.columns(2)


    with col1:

        st.success(
            f"✅ Exception\n\n"
            f"{log['Exception']}"
        )


    with col2:

        st.warning(
            f"⚠ Failure Point\n\n"
            f"{log['Failure Point']}"
        )


    st.info(
        f"📍 Affected Code Path : "
        f"{log['Affected Code Path']}"
    )


    # =====================================================
    # ROOT CAUSE AGENT
    # =====================================================

    st.divider()

    st.subheader("🧠 Root Cause Agent")

    root = analysis["Root Cause Agent"]

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🎯 Confidence",
            f"{root['Confidence']}%"
        )

        st.progress(
            root["Confidence"] / 100
        )


    with col2:

        st.success(
            f"🛠 Root Cause\n\n"
            f"{root['Root Cause']}"
        )


    with col3:

        st.info(
            "📚 Historical Evidence"
        )


    evidence = root["Evidence"]

    if evidence:

        st.write(
            str(evidence)[:200] + "..."
        )


    with st.expander("📖 Show More"):

        st.write(evidence)


    # =====================================================
    # DUPLICATE DETECTION AGENT
    # =====================================================

    st.divider()

    st.subheader(
        "🔍 Duplicate Detection Agent"
    )

    duplicates = analysis[
        "Duplicate Detection Agent"
    ]


    if duplicates:

        for bug in duplicates:

            with st.expander(
                f"🐞 Duplicate Bug {bug['Bug ID']}"
            ):

                col1, col2 = st.columns(2)


                with col1:

                    st.metric(
                        "Similarity",
                        bug["Similarity"]
                    )


                with col2:

                    st.success(
                        "Historical Match Found"
                    )


                st.write(
                    "### 📄 Historical Resolution Summary"
                )

                st.write(
                    bug["Historical Summary"]
                )

    else:

        st.info(
            "No duplicate bugs detected."
        )


    # =====================================================
    # REMEDIATION AGENT
    # =====================================================

    st.divider()

    st.subheader("🛠️ Remediation Agent")

    remedy = analysis["Remediation Agent"]

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Confidence",
            f"{remedy['Confidence']}%"
        )

        st.progress(
            remedy["Confidence"] / 100
        )


    with col2:

        st.success(
            remedy["Recommended Fix"]
        )


    st.info(
        f"💡 Best Practice : "
        f"{remedy['Best Practice']}"
    )


    # =====================================================
    # KNOWLEDGE BASE GROWTH
    # =====================================================

    st.divider()

    st.subheader(
        "📚 Knowledge Base Growth"
    )

    st.write(
        "If the recommended fix successfully resolved "
        "the bug, confirm it below to add the resolved "
        "bug to the knowledge base."
    )


    fix_confirmed = st.checkbox(
        "✅ Confirm that the recommended fix resolved this bug",
        key="fix_confirmed_checkbox"
    )


    if fix_confirmed:

        resolved_bug = {

            "Title": bug_title,

            "Description":
                bug_description,

            "Exception":
                log["Exception"],

            "Root Cause":
                root["Root Cause"],

            "Recommended Fix":
                remedy["Recommended Fix"],

            "Best Practice":
                remedy["Best Practice"],

            "Confirmed":
                True
        }


        if not st.session_state.knowledge_base_added:

            try:

                add_resolved_bug(
                    resolved_bug
                )

                st.session_state.knowledge_base_added = True

                st.success(
                    "✅ Resolved bug added to the knowledge base successfully!"
                )

            except Exception as e:

                st.error(
                    f"❌ Failed to update knowledge base: {e}"
                )

        else:

            st.success(
                "✅ This resolved bug is already added to the knowledge base."
            )


    # =====================================================
    # HISTORICAL SIMILAR BUGS
    # =====================================================

    st.divider()

    st.subheader(
        "📚 Historical Similar Bugs"
    )


    results = search_similar_bugs(
        bug_description
    )


    if results:

        for i, bug in enumerate(results):

            with st.expander(
                f"🐞 Similar Bug {i + 1}"
            ):

                st.code(bug)

    else:

        st.info(
            "No similar historical bugs found."
        )


    # =====================================================
    # STRUCTURED FINDINGS SUMMARY
    # =====================================================

    st.divider()

    st.header(
        "📋 Structured Findings Summary"
    )


    summary = {

        "Severity":
            triage["Severity"],

        "Priority":
            triage["Priority"],

        "Component":
            triage["Component"],

        "Exception":
            log["Exception"],

        "Failure Point":
            log["Failure Point"],

        "Affected Code Path":
            log["Affected Code Path"],

        "Root Cause":
            root["Root Cause"],

        "Root Cause Confidence":
            f"{root['Confidence']}%",

        "Recommended Fix":
            remedy["Recommended Fix"],

        "Remediation Confidence":
            f"{remedy['Confidence']}%"
    }


    st.json(summary)


    # =====================================================
    # DEFECT PATTERN ANALYTICS
    # =====================================================

    st.divider()

    st.header(
        "📊 Defect Pattern Analytics"
    )


    patterns = analyze_defect_patterns()


    if patterns["total_bugs"] == 0:

        st.info(
            "No bug history available yet."
        )

    else:

        st.metric(
            "🐞 Total Bugs Analyzed",
            patterns["total_bugs"]
        )


        # -------------------------------------------------
        # SEVERITY PATTERNS
        # -------------------------------------------------

        st.subheader(
            "🔥 Severity Distribution"
        )

        severity_data = patterns[
            "severity_patterns"
        ]

        if severity_data:

            st.bar_chart(
                severity_data
            )


        # -------------------------------------------------
        # COMPONENT PATTERNS
        # -------------------------------------------------

        st.subheader(
            "🧩 Most Affected Components"
        )

        component_data = patterns[
            "component_patterns"
        ]

        if component_data:

            st.bar_chart(
                component_data
            )


        # -------------------------------------------------
        # EXCEPTION PATTERNS
        # -------------------------------------------------

        st.subheader(
            "⚠️ Common Exceptions"
        )

        exception_data = patterns[
            "exception_patterns"
        ]

        if exception_data:

            st.bar_chart(
                exception_data
            )


        # -------------------------------------------------
        # ROOT CAUSE PATTERNS
        # -------------------------------------------------

        st.subheader(
            "🧠 Common Root Causes"
        )

        root_cause_data = patterns[
            "root_cause_patterns"
        ]

        if root_cause_data:

            st.bar_chart(
                root_cause_data
            )


        # -------------------------------------------------
        # PATTERN SUMMARY
        # -------------------------------------------------

        st.subheader(
            "📋 Pattern Summary"
        )


        most_common_severity = (

            max(
                severity_data,
                key=severity_data.get
            )

            if severity_data

            else "N/A"
        )


        most_affected_component = (

            max(
                component_data,
                key=component_data.get
            )

            if component_data

            else "N/A"
        )


        most_common_exception = (

            max(
                exception_data,
                key=exception_data.get
            )

            if exception_data

            else "N/A"
        )


        most_common_root_cause = (

            max(
                root_cause_data,
                key=root_cause_data.get
            )

            if root_cause_data

            else "N/A"
        )


        st.write(
            f"🔥 **Most Common Severity:** "
            f"{most_common_severity}"
        )

        st.write(
            f"🧩 **Most Affected Component:** "
            f"{most_affected_component}"
        )

        st.write(
            f"⚠️ **Most Common Exception:** "
            f"{most_common_exception}"
        )

        st.write(
            f"🧠 **Most Common Root Cause:** "
            f"{most_common_root_cause}"
        )


    # =====================================================
    # END-TO-END TESTING & VALIDATION
    # =====================================================

    st.divider()

    st.header(
        "🧪 End-to-End Testing & Validation"
    )

    st.write(
        "Validation of the complete bug analysis pipeline "
        "using submitted bug reports."
    )


    validation = validate_bug_history()


    # -----------------------------------------------------
    # TOTAL BUGS
    # -----------------------------------------------------

    st.metric(
        "🐞 Total Bug Submissions",
        validation["total_bugs"]
    )


    # -----------------------------------------------------
    # MINIMUM FIVE BUGS CHECK
    # -----------------------------------------------------

    if validation["minimum_five_bugs"]:

        st.success(
            "✅ Minimum 5 distinct bug submissions requirement satisfied."
        )

    else:

        st.warning(
            f"⚠️ Only {validation['total_bugs']} bug(s) found. "
            "Minimum 5 required."
        )


    # -----------------------------------------------------
    # PIPELINE VALIDATION
    # -----------------------------------------------------

    st.subheader(
        "🔍 Agent Pipeline Validation"
    )


    if validation["all_fields_valid"]:

        st.success(
            "✅ All required agent outputs are available "
            "for the submitted bugs."
        )

    else:

        st.warning(
            "⚠️ Some bug records have missing fields."
        )


    # -----------------------------------------------------
    # BUG-BY-BUG RESULTS
    # -----------------------------------------------------

    st.subheader(
        "📋 Bug Validation Results"
    )


    for bug in validation["bugs"]:

        if bug["Status"] == "PASS":

            st.success(
                f"Bug {bug['Bug Number']}: "
                f"{bug['Title']} — PASS ✅"
            )

        else:

            st.error(
                f"Bug {bug['Bug Number']}: "
                f"{bug['Title']} — FAIL ❌"
            )

            st.write(
                "Missing fields:",
                bug["Missing Fields"]
            )


    # -----------------------------------------------------
    # REQUIRED AGENTS
    # -----------------------------------------------------

    st.subheader(
        "🤖 Required Agent Checks"
    )


    agent_checks = {

        "Triage Agent": True,

        "Log Analysis Agent": True,

        "Root Cause Agent": True,

        "Duplicate Detection Agent": True,

        "Remediation Agent": True
    }


    for agent, status in agent_checks.items():

        if status:

            st.write(
                f"✅ {agent}"
            )

        else:

            st.write(
                f"❌ {agent}"
            )


    # -----------------------------------------------------
    # FINAL VALIDATION
    # -----------------------------------------------------

    if (
        validation["minimum_five_bugs"]
        and validation["all_fields_valid"]
    ):

        st.success(
            "🎉 END-TO-END TESTING PASSED"
        )

        st.write(
            "The system was tested using multiple bug types "
            "and the required agent pipeline outputs were validated."
        )

    else:

        st.warning(
            "⚠️ END-TO-END TESTING INCOMPLETE"
        )