import streamlit as st
from agent import Agent

st.set_page_config(page_title="AI Code Review Dashboard", layout="wide")

st.title("🤖 AI Code Review Dashboard")

# ----------------------------
# INPUT
# ----------------------------
code = st.text_area("Enter Code", height=250)

# ----------------------------
# RUN ANALYSIS
# ----------------------------
if st.button("Analyze"):

    if not code.strip():
        st.warning("Please enter some code to analyze.")
        st.stop()

    agent = Agent()
    result = agent.run(code)

    static = result.get("static", {})
    ai = result.get("ai_review", {})

    # =========================
    # 📊 STATIC ANALYSIS
    # =========================
    st.header("📊 Static Analysis")

    st.subheader("Language")
    st.write(static.get("language", "Unknown"))

    st.subheader("Complexity")
    st.json(static.get("complexity", {}))

    st.subheader("AST (Basic Analysis)")
    st.json(static.get("ast", {}))

    st.subheader("🔴 Critical Bugs")
    st.json(static.get("critical_bugs", []))

    st.subheader("🟡 Warnings")
    st.json(static.get("warnings", []))

    # =========================
    # 🧠 AI REVIEW
    # =========================
    st.header("🧠 AI Review")

    st.markdown("### 📌 Summary")
    st.write(ai.get("summary", "No summary available"))

    st.markdown("### 🐞 Bugs Explained")
    st.write(ai.get("bugs_explained", "No explanation available"))

    st.markdown("### ⚠️ Severity Analysis")
    st.write(ai.get("severity_analysis", "N/A"))

    st.markdown("### 📚 Suggestions")
    suggestions = ai.get("suggestions", "")
    if isinstance(suggestions, list):
        st.write("\n".join(str(x) for x in suggestions))
    else:
        st.write(suggestions)

    st.markdown("### 🔧 Fix Explanation")
    st.write(ai.get("fix_explanation", "N/A"))

    # =========================
    # 🔧 FINAL FIXED CODE
    # =========================
    st.header("🔧 Final Fixed Code")

    fixed_code = result.get("final_fixed_code", "")

    if fixed_code:
        st.code(fixed_code, language=static.get("language", "text"))
    else:
        st.info("No fixed code generated.")