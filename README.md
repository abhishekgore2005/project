📄 AI-Powered HR Resume Screening System
This project is a Natural Language Processing (NLP) tool built to automate the initial screening of resumes. It specifically differentiates between technical and managerial roles based on a Comparative Analysis of industry requirements.

🚀 Features

PDF Text Extraction: Seamlessly parses data from uploaded resumes using pypdf.


Intelligent Scoring: Uses TF-IDF Vectorization and Cosine Similarity to mathematically rank resumes against specific job descriptions.



Dual-Role Analysis: Simultaneously compares candidates against two distinct career paths:


Role A: Technical Systems Support (The "Engine Mechanic").



Role B: IT Management & Strategy (The "Fleet Commander").


Web Interface: A user-friendly dashboard built with Streamlit for real-time file processing.

🧠 The Logic
The system's "brain" is grounded in the research processed via NotebookLM, which identified key differentiators between technical and leadership roles.

Vectorization: The system converts text into numerical vectors. It assigns higher "weights" to specific technical tools (like VMware or PowerShell) for Role A and strategic frameworks (like ITIL or Scrum) for Role B.



Similarity Calculation: By calculating the "Cosine Similarity," the system measures the alignment of a candidate's experience with the required job profile.

🛠️ Technical Stack
Language: Python

Library (NLP/ML): Scikit-learn (TfidfVectorizer, Cosine Similarity)

Library (Parsing): PyPDF2 / pypdf

Framework: Streamlit (Web UI)

Knowledge Management: NotebookLM (Research & Documentation)

📋 Installation & Usage
Clone the repository:



git clone https://github.com/yourusername/resume-screener.git
Install dependencies:



pip install -r requirements.txt
Run the application:



streamlit run app.py
📈 Research Insights
According to the comparative analysis:





Technical Support roles focus on troubleshooting, hardware maintenance, and network security.



IT Management roles prioritize budget administration, vendor negotiation, and staff development.
