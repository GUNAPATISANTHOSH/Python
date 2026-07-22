from docx import Document
from fpdf import FPDF

# Create a formatted resume content
resume_content = """
GUNAPATI SANTHOSH REDDY
📍 Khajipet, Andhra Pradesh – 516203
📞 +91-9347471912
📧 santoshsantutej@gmail.com
🔗 linkedin.com/in/santoshsantutej

CAREER OBJECTIVE
Motivated and diligent undergraduate student in Computer Science and Engineering, seeking opportunities to apply technical and analytical skills in a challenging and growth-oriented environment. Eager to contribute to innovative projects while gaining practical experience and expanding expertise.

EDUCATION
- B.E. – Computer Science and Engineering, Saveetha School of Engineering (Autonomous), 2026 (Expected) – CGPA: 8.14
- Intermediate (MPC), Narayana Junior College, State Board, 2022 – 82%
- SSC, A.P Model School, State Board, 2020 – GPA: 9.7

TECHNICAL SKILLS
- Languages: C, C++, Python (Basic)
- Web Technologies: HTML, CSS
- Tools & Platforms: Power BI (Introductory), MySQL, XAMPP Server

PROJECTS
1. Fake Currency Detection Using Image Processing (Minor Project)
   - Used image processing techniques to analyze currency features such as watermarks, colors, and security threads.
   - Aimed at distinguishing counterfeit currency using pattern recognition.

2. Automated CAPTCHA Recognition Using Deep Learning (Major Project - Ongoing)
   - Biometric authentication system using palm vein pattern recognition.
   - Utilizes NIR imaging and deep learning for feature extraction and verification.

3. Online E-Commerce Website
   - Developed a basic shopping website to simulate user interactions like product browsing, cart management, and checkout.
   - Demonstrated core understanding of front-end design and user experience.

CERTIFICATIONS
- Workshop on KUKA ROBOTICS, Jarvis’25 – Chennai Institute of Technology (12-Feb-2025)
- Data Analytics Using Power BI – 4-hour workshop with end-to-end project by TechTip24

LANGUAGES
- Telugu – Native
- English – Speak, Read, Write

INTERESTS & HOBBIES
- Listening to Music 🎧
- Gaming 🎮
- Watching Anime 📺

DECLARATION
I hereby declare that the above information is true and correct to the best of my knowledge and belief.
Place: Khajipet, Andhra Pradesh
Signature: G. Santhosh Reddy
"""

# Create a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=11)

# Add content line by line
for line in resume_content.strip().split('\n'):
    pdf.multi_cell(0, 10, line.strip())

# Save the PDF
pdf_path = "/mnt/data/Gunapati_Santhosh_Reddy_Resume.pdf"
pdf.output(pdf_path)

pdf_path