import streamlit as st

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="GradPilot AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

h1, h2, h3 {
    color: #38bdf8;
}

.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    padding: 10px;
}

.stButton button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px 20px;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.title("🎓 GradPilot AI")
st.subheader("Your AI Academic Co-Pilot 🚀")

st.markdown("---")

# ---------------- INPUT ---------------- #
query = st.text_input("🔍 Ask your academic query")

# ---------------- BUTTON ---------------- #
if st.button("⚡ Generate Smart Plan"):
    
    # Simulated outputs (replace with your logic)
    notes = "• DBMS includes normalization, indexing, SQL queries...\n• Transactions ensure ACID properties..."
    
    timetable = """
Day 1: Basics + ER Model  
Day 2: SQL + Queries  
Day 3: Normalization  
Day 4: Transactions  
Day 5: Revision + Practice
    """

    # ---------------- OUTPUT LAYOUT ---------------- #
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📘 Smart Notes")
        st.write(notes)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📅 Study Plan")
        st.write(timetable)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- AUDIT TRAIL ---------------- #
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚙️ AI Workflow (Audit Trail)")
    st.write("""
    ✔ Query Agent → Understands input  
    ✔ Retrieval Agent → Fetches data  
    ✔ Content Agent → Generates notes  
    ✔ Planner Agent → Creates timetable  
    ✔ Validator Agent → Ensures quality  
    """)
    st.markdown('</div>', unsafe_allow_html=True)