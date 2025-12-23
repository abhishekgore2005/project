import streamlit as st
import pypdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- PHASE 1 DATA INTEGRATION ---
# These JDs are built directly from your Comparative Analysis research [cite: 3, 4]
job_descriptions = {
    "Technical Systems Support (Role A)": """
    Troubleshooting and maintaining hardware, software, and network security[cite: 5]. 
    Active Directory, Group Policy, VMware, PowerShell, VBScript[cite: 6]. 
    LAN/WAN connectivity, TCP/IP protocols, VPN[cite: 10]. 
    Focus on diagnostics, system analysis, and scripting like Python/SQL[cite: 9, 14].
    """,
    "IT Management (Role B)": """
    Strategic planning, risk mitigation, and cost-effective solutions[cite: 5]. 
    Budget administration, vendor selection, contract management[cite: 7]. 
    Staff development, hiring, and building cross-functional teams[cite: 8]. 
    Waterfall framework, Scrum methodology, and ITIL processes[cite: 9]. 
    Disaster recovery planning and architecture re-engineering[cite: 10].
    """
}

# --- HELPER FUNCTIONS ---
def extract_text_from_pdf(file):
    pdf_reader = pypdf.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def calculate_match(resume_text, jd_text):
    corpus = [jd_text, resume_text]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    vectors = vectorizer.toarray()
    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    return round(score * 100, 2)

# --- STREAMLIT UI ---
st.set_page_config(page_title="AI Resume Screener", page_icon="📄")
st.title("HR Resume Screening System")
st.subheader("Comparative Analysis: Support vs. Management")

uploaded_file = st.file_uploader("Upload a Resume (PDF)", type="pdf")

if uploaded_file is not None:
    with st.spinner('Analyzing Resume...'):
        # 1. Extract
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # 2. Score
        st.write("### Analysis Results")
        col1, col2 = st.columns(2)
        
        for i, (role, jd) in enumerate(job_descriptions.items()):
            score = calculate_match(resume_text, jd)
            
            # Display result in columns
            if i == 0:
                col1.metric(label=role, value=f"{score}%")
            else:
                col2.metric(label=role, value=f"{score}%")
        
        # 3. Role-Specific Insight based on research 
        st.divider()
        if score > 50: # Example threshold
             st.info("**AI Insight:** This candidate shows strong alignment with the 'Fleet Commander' profile, focusing on strategic oversight.")
        else:
             st.info("**AI Insight:** This candidate aligns more with the 'Engine Mechanic' profile, focusing on core component functionality.")

st.sidebar.markdown("""
**How it works:**
This system uses **TF-IDF Vectorization** to compare the mathematical 'fingerprint' 
of a resume against specific Job Descriptions derived from your research.
""")