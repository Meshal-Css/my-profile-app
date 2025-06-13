import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_timeline import timeline
import json
import base64

# ---------- إعدادات الصفحة ----------
st.set_page_config(page_title="My Profile", layout="wide")

# ---------- القائمة الجانبية ----------
with st.sidebar:
    selected = option_menu(
        None,
        ["Profile", "Skills", "Projects", "Contact Me"],
        icons=["person-circle", "bar-chart-line", "kanban", "envelope"],
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#0e1117"},
            "icon": {"color": "#F8F9FA", "font-size": "20px"},
            "nav-link": {
                "color": "#F8F9FA",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#04B4F5",
            },
            "nav-link-selected": {"background-color": "#0F2D38"},
        },
    )

# ---------- الصفحة الأولى: الملف الشخصي ----------
if selected == "Profile":
    st.title("My Profile")

    try:
        with open("image1.jpg", "rb") as img_file:
            img_data = base64.b64encode(img_file.read()).decode()

        st.markdown(f"""
            <div style='background-color: #000000; padding: 20px; border-radius: 10px; border: 2px solid #00BFFF; display: flex; align-items: center; gap: 30px;'>
                <div style='flex: 1;'>
                    <img src='data:image/jpeg;base64,{img_data}' style='width: 100%; border-radius: 10px;' />
                </div>
                <div style='flex: 2;'>
                    <h2 style='font-size: 24px; color: #F8F9FA;'>Career Objective</h2>
                    <p style='font-size: 22px; color: #F8F9FA;'>
                        A driven Data Analyst with a strong background in Computer Science and practical experience in data analysis, AI, and project development.
                        Completed SDAIA T5 Bootcamp, gaining solid skills in Python, SQL, machine learning, and deep learning.
                        Led team-based projects and developed innovative AI-driven solutions to enhance decision-making.
                        Passionate about transforming data into actionable insights and building impactful technologies.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("❌ لم يتم العثور على الصورة 'image1.jpg'. تأكد من أنها موجودة في نفس مجلد الملف.")

    st.subheader("Career Journey Timeline")

    career_data = {
        "title": "Career Timeline",
        "events": [
            {"start_date": {"year": 2023, "month": 9}, "text": {"headline": "Joined SDAIA Academy", "text": "Started training in AI, data science, and machine learning."}},
            {"start_date": {"year": 2024, "month": 1}, "text": {"headline": "Developed RCT Project", "text": "Road Condition Tracker selected among top projects."}},
            {"start_date": {"year": 2024, "month": 5}, "text": {"headline": "Presented RCT to Judges", "text": "Presented smart traffic solution using YOLO and GPS in final pitch."}},
            {"start_date": {"year": 2024, "month": 6}, "text": {"headline": "Began Internship", "text": "Joined Tuwaiq Traffic Tech Bootcamp as intern working on traffic analytics."}},
            {"start_date": {"year": 2025, "month": 3}, "text": {"headline": "Target: Join Riyad Bank", "text": "Aiming to work on AI-powered financial analytics and smart data systems."}}
        ]
    }

    timeline(json.dumps(career_data), height=500)

# ---------- الصفحة الثانية: المهارات ----------
elif selected == "Skills":
    st.title("Skills")

    skills = [
        {"title": "Python", "desc": "Data analysis, automation, AI"},
        {"title": "SQL", "desc": "Relational databases, joins, queries"},
        {"title": "Power BI", "desc": "Interactive dashboards & reports"},
        {"title": "Machine Learning", "desc": "Classification, Regression, Clustering"},
        {"title": "Streamlit", "desc": "Build beautiful data apps easily"},
        {"title": "Data Analysis", "desc": "EDA, insights extraction, visualization"},
    ]

    st.markdown("""
        <style>
        .skill-card {
            border: 2px solid #00BFFF;
            border-radius: 15px;
            padding: 20px;
            background-color: #000000;
            color: white;
            transition: transform 0.3s ease;
            cursor: pointer;
        }
        .skill-card:hover {
            transform: scale(1.05);
            border-color: #1E90FF;
        }
        </style>
    """, unsafe_allow_html=True)

    cols = st.columns(3)
    for i, sk in enumerate(skills):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="skill-card">
                <h4>{sk['title']}</h4>
                <p>{sk['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------- الصفحة الثالثة: المشاريع ----------
elif selected == "Projects":
    st.title("Projects")

    st.subheader("RCT – Road Condition Tracker")
    st.write("AI system to detect and report potholes in Riyadh using YOLOv8 and GPS with Raspberry Pi.")

    st.subheader("Weather & Air Quality Analysis")
    st.write("Analyzed Riyadh weather and PM2.5 pollution data to understand impact on public health.")

    st.subheader("Bus Breakdown Prediction")
    st.write("Built predictive models for bus delays and breakdowns using time-series sensor data.")

# ---------- الصفحة الرابعة: تواصل معي ----------
elif selected == "Contact Me":
    st.title("Contact Me")
    st.write("Feel free to reach out via the following channels:")

    try:
        with open("cv.pdf", "rb") as file:
            cv_data = file.read()
            cv_base64 = base64.b64encode(cv_data).decode()
    except FileNotFoundError:
        cv_base64 = None
        st.warning("⚠️ CV file (Meshal Saud Aldalbahi.pdf) not found. Please add it to the project directory.")

    st.markdown("""
        <style>
        .btn-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 30px;
        }
        .btn-circle {
            width: 100px;
            height: 100px;
            background-color: #000000;
            color: #FFFFFF;
            border: 2px solid #00BFFF;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .btn-circle:hover {
            background-color: #1E90FF;
            color: #fff;
            transform: scale(1.1);
        }
        </style>
    """, unsafe_allow_html=True)

    contact_html = """
        <div class="btn-container">
            <a class="btn-circle" href="https://www.linkedin.com/in/meshalaldalbahi" target="_blank">LinkedIn</a>
            <a class="btn-circle" href="https://github.com/Meshal-Css" target="_blank">GitHub</a>
            <a class="btn-circle" href="mailto:meshal.sau.alotaibi@gmail.com">Email</a>
    """



    st.markdown(contact_html, unsafe_allow_html=True)
