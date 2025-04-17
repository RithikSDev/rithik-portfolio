import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Rithik's Portfolio", layout="wide")

# -------------------------------
# Function to load Lottie animation
# -------------------------------
def load_lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css(r"C:\Users\rithi\Desktop\portfolio\style\style.css")        


# Assets
lottie_coder = load_lottieurl("https://lottie.host/c2a11e3e-fcd3-4c6b-8bf7-541cff9979c7/BFNiXyOoLM.json")
lottie_contact= load_lottieurl("https://lottie.host/bebf0f77-6e9f-44d8-894f-6bf0e0135fc6/m8Oy4A3hHT.json")
image_1 = Image.open(r"C:\Users\rithi\Desktop\portfolio\senti.png")



# Hero Section
# -------------------------------
st.write("##")
st.subheader("Hey Guys... :wave:")
st.title("My Portfolio Website")

st.write("""
I'm a **Data Analyst (Analytics)** at **KultureHire**, and I proudly serve as the **Lead Data Analyst & Zone Head – Coimbatore** for the prestigious **Naan Mudhalvan Project** – a Government of Tamil Nadu initiative focused on student empowerment through skill development.

🔍 In my role, I lead **data-driven strategies** and oversee **analytics operations across 18+ institutions**, helping create measurable impact in education.

💻 I also bring hands-on experience in **Odoo Development**, having built custom modules for:
- **Subscription Management**
- **Security Role Management**
- **Advanced Search Filters**
""")

st.write("---")

st.header("🔧 Technical Skillset & Specializations")
st.write("""
With a strong foundation in **Python**, **Power BI**, **MongoDB**, **Streamlit**, **Odoo Development**, and **SQL**, I specialize in:

- 🧠 Building **Predictive Models** for actionable insights  
- 📊 Designing **Interactive Dashboards** for smarter decision-making  
- ⚙️ Developing **Automation Solutions** to streamline business operations
""")

st.write("---")

st.info("My mission is to harness data and technology to solve real-world problems and drive meaningful change in both education and business.")

st.markdown("---")

# -------------------------------
# Navigation Menu
# -------------------------------
selected = option_menu(
    menu_title=None,
    options=["About", "Projects", "Contact"],
    icons=["person", "code-slash", "chat-left-text-fill"],
    orientation="horizontal"
)

# -------------------------------
# About Section
# -------------------------------
if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Hi, I'm Rithik S. 👋")
            st.write("### Data Analyst | Python Developer")
            st.write("""
I'm a tech enthusiast with experience in Data Analytics, Python Development, and AI-powered solutions.

I work as a **Data Analyst Trainer at KultureHire**, teaching Power BI, SQL, and Excel.  
I'm also the **Zone Head of Coimbatore** for the **Naan Mudhalvan Project**, leading data-driven strategies for 18+ colleges.

Projects I’ve built:
- **Customer Churn Prediction**
- **RAG-based ChatBot using Hugging Face**
- **Speech-to-Text/Voice Cloning System**
- **Custom Odoo Modules for ERP Solutions**

💡 Passionate about turning data into insights, developing cool tools, and helping others grow in tech.

📫 Reach me at: `rithik.s.1207@gmail.com`  
🔗 [LinkedIn](https://linkedin.com/in/rithik-s-02372118a) | [GitHub](https://github.com/RithikSDev)
""")
        with col2:
            if lottie_coder:
                st_lottie(lottie_coder, height=300, key="coder")

    st.markdown("---")

    # -------------------------------
    # Education & Experience
    # -------------------------------
    with st.container():
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("""
### 🎓 Education
**SNS College of Engineering**  
Bachelor of Technology – Artificial Intelligence and Data Science (2020–2024)  
*C.G.P.A: 7.9*

**MALCO Vidyalaya Matric Hr. Sec. School**  
Grade: 75%
""")
        with col4:
            st.markdown("""
### 💼 Experience
**Data Analyst – KultureHire**  
_Remote | 2024 - Present_

- Conducting training on data tools like Power BI and SQL.
- Handling data for institutional and government analytics initiatives.
""")

# -------------------------------
# Projects Section
# -------------------------------
elif selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns([1, 2])
        with col5:
            st.image(image_1)
        with col6:
            st.markdown("""
#### 💼 Sentiment Review Response Generator

An **AI-powered NLP application** that leverages **transformer-based models** to automate sentiment classification and contextual response generation for customer reviews. Designed for scalability and ease of use in **customer support workflows**.

**🔧 Technical Highlights:**
- ✅ **Sentiment Classification** using `distilBERT` via Hugging Face's `transformers` pipeline  
- 🧠 **Context-aware Response Generation** using rule-based logic with NLP templates   
- 🌈 **Custom Streamlit Frontend** styled with advanced **CSS overrides** for a modern user interface  
- ⚙️ Modular architecture with separation of logic (`utils.py`) and UI (`main.py`)

**📁 Tech Stack:** `Python`, `Streamlit`, `Transformers`, `Pandas`, `NLP`, `CSV Logging`


🌐 [Live Demo on Streamlit Cloud](https://sentiment-review-response.streamlit.app/)
""")
# -------------------------------
# Contact Section (Optional)
# -------------------------------
if selected == "Contact":
    st.header("Get in Touch!")
    contact_form = """
<form action="https://formsubmit.co/rithik.s.1207@gmail.com" method="POST" style="margin: auto;">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""

  # Side-by-side layout
    left_col, right_col = st.columns([2, 1], gap="large")

    with left_col:
        st.markdown("### Drop a message 👇")
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_col:
        st_lottie(lottie_contact, height=100)