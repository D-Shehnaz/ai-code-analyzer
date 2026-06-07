import streamlit as st
from agent import Agent

st.set_page_config(
    page_title="AI Code Review Dashboard",
    layout="wide"
)

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
    result = agent.run(code) or {}

    # ----------------------------
    # SAFE EXTRACTION
    # ----------------------------
    static = result.get("static") or {}
    ai = result.get("ai_review") or {}

    critical = result.get("critical_bugs") or []
    warnings = result.get("warnings") or []
    severity_score = result.get("severity_score") or 0

    # AI fields (fully safe)
    summary = ai.get("summary") or "No summary available"
    bugs_explained = ai.get("bugs_explained") or ""
    severity_analysis = ai.get("severity_analysis") or ""
    suggestions = ai.get("suggestions") or []
    fix_explanation = ai.get("fix_explanation") or ""

    # FIXED CODE (extra safety)
    fixed_code = (result.get("fixed_code") or ai.get("fixed_code") or "").strip()

    # =========================
    # 📊 STATIC ANALYSIS
    # =========================
    st.header("📊 Static Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Language")
        st.success(static.get("language") or "Unknown")

    with col2:
        st.subheader("Severity Score")
        st.metric("Risk Level", f"{severity_score}/100")

    with col3:
        st.subheader("Complexity Score")
        st.metric("Score", static.get("complexity", {}).get("score", 0))

    st.divider()

    # AST
    st.subheader("🧠 AST Analysis")
    st.json(static.get("ast") or {})

    # Complexity
    st.subheader("⚙️ Complexity Breakdown")
    st.json(static.get("complexity") or {})

    # =========================
    # 🚨 BUGS SECTION
    # =========================
    st.header("🚨 Detected Issues")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔴 Critical Issues")

        if critical:
            for b in critical:
                st.error(f"{b.get('type', 'unknown')} - {b.get('message', '')}")
        else:
            st.success("No critical issues found.")

    with col2:
        st.subheader("🟡 Warnings")

        if warnings:
            for w in warnings:
                st.warning(f"{w.get('type', 'unknown')} - {w.get('message', '')}")
        else:
            st.success("No warnings found.")

    # =========================
    # 🧠 AI REVIEW
    # =========================
    st.header("🧠 AI Review")

    st.markdown("### 📌 Summary")
    st.info(summary)

    if bugs_explained:
        st.markdown("### 🐞 Bugs Explained")
        st.write(bugs_explained)

    if severity_analysis:
        st.markdown("### ⚠️ Severity Analysis")
        st.write(severity_analysis)

    # AI findings (safe iteration)
    st.markdown("### 🔍 AI Findings")

    ai_findings = ai.get("findings") or []
    if ai_findings:
        for f in ai_findings:
            st.write(f"• **{f.get('type', 'unknown')}** → {f.get('message', '')}")
    else:
        st.write("No AI findings.")

    # suggestions
    if suggestions:
        st.markdown("### 📚 Suggestions")
        for s in suggestions:
            st.write("✔", s)

    # fix explanation
    if fix_explanation:
        st.markdown("### 🔧 Fix Explanation")
        st.write(fix_explanation)

    # =========================
    # 🔧 FIXED CODE
    # =========================
    st.header("🔧 Suggested Fixed Code")

    if fixed_code and len(fixed_code) > 3:
        st.code(fixed_code, language=static.get("language", "text"))
    else:
        st.info("No fixed code generated.")