import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_timeline import timeline
import json
import base64

# إعدادات الصفحة
st.set_page_config(page_title="My Profile", layout="wide")

# القائمة الجانبية
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

# الصفحة الأولى: الملف الشخصي
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
                    <h2 style='font-size: 24px; color: #F8F9FA;'>Who am I?</h2>
                    <p style='font-size: 22px; color: #F8F9FA;'>
                        I am Meshal, a specialist in data analysis. I wanted to design this website that reflects a simple thing of my orientation and goals in the field that I consider to be a passion for achievement. The term data analysis may seem to you to be a practical concept, but for me, data analysis made me look at it from a different angle. It made me search for details, address errors, and reach fruitful results. Data analysis taught me the joy of achievement in the end. This website is presented in a message to you. Who am I? What do I want to be in the future? Where have I reached? Welcome.
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("لم يتم العثور على الصورة 'image1.jpg'. تأكد من أنها موجودة في نفس مجلد الملف.")

    st.subheader("Journey Timeline")

    career_data = {
        "title": {
            "text": {
                "headline": "My journey to my goals",
                "text": "Swipe to start learning my story."
            }
        },
        "events": [
            {"start_date": {"year": 2024, "month": 6}, "text": {"headline": "My graduation from university and the beginning of my journey", "text": "My journey began with the end of my university journey and academic path in June 2024 to begin towards the beginning of my dream"}},
            {"start_date": {"year": 2024, "month": 7}, "text": {"headline": "Join the Congestion Management Techniques Camp provided by SDAIA", "text": "After university, I started working in the field where I feel the pleasure of accomplishment, which is working in the field of data science and artificial intelligence, to start learning and working with an elite group of heroes who were a source of inspiration for me."}},
            {"start_date": {"year": 2024, "month": 8}, "text": {"headline": "Working on a project specializing in congestion management", "text": "After the learning journey in the camp, we started to achieve the camp’s goal and work on a project that would help solve part of the traffic congestion problems. I met with my team members and wrote down our ideas. After the experience of living in the city of Riyadh, I realized that there are some construction and road wastes that have a direct impact on obstructing the roads. We started to analyze and collect the necessary data."}},
            {"start_date": {"year": 2024, "month": 9}, "text": {"headline": "Camp Project Delivery Our Story Our Project RCT", "text": "This month we selected our project after a journey of data collection, analysis and data processing. It confirmed to us that yes, there is a direct cause of road waste and congestion. We started our project with Road Condition Tracker and worked on it. My team and I did not aim to finish the project, we were only looking for a solution to an actual problem. In the end, our project was selected among the distinguished projects in the camp."}},
            {"start_date": {"year": 2025, "month": 3}, "text": {"headline": "Join the Ai World Journey Camp", "text": "I didn't stop there and I don't think I'll ever announce it! I joined this camp after extensive practice in the field of AI. The camp was offered by the Artificial Intelligence Governance Association and I created a new system that uses computer vision to identify the duration of an employee's phone use during their work period. The goal of this project was to raise the quality of work within the organization's environment and I received a certificate for project excellence."}}
        ],
        "theme": {
            "textColor": "#FFFFFF",
            "background": "#000000",
            "accentColor": "#00BFFF"
        }
    }

    timeline(json.dumps(career_data), height=500)

# الصفحة الثانية: المهارات
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

# الصفحة الثالثة: المشاريع
elif selected == "Projects":
    st.title("Projects")

    try:
        with open("project theme.png", "rb") as banner:
            banner_data = base64.b64encode(banner.read()).decode()
            st.markdown(
                f"<img src='data:image/jpeg;base64,{banner_data}' style='width: 100%; border-radius: 15px; margin-bottom: 30px;'>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("صورة الثيم 'project theme.png' غير موجودة. الرجاء إضافتها إلى مجلد المشروع.")

    st.markdown("""
        <style>
        .project-card {
            border: 2px solid #00BFFF;
            border-radius: 15px;
            padding: 20px;
            background-color: #000000;
            color: white;
            transition: transform 0.3s ease;
            cursor: pointer;
            margin-bottom: 20px;
        }
        .project-card:hover {
            transform: scale(1.03);
            border-color: #1E90FF;
        }
        .project-header {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .project-logo {
            width: 60px;
            height: 60px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("""
       <div class="project-card">
    <div class="project-header">
        <h4>YOLOv8 Pothole Detection</h4>
    </div>
    <a href="https://blank-app-qubcsndeg5.streamlit.app" target="_blank">
        <button style="margin-top: 10px; padding: 10px 20px; font-size: 16px; border-radius: 8px; background-color: #4CAF50; color: white; border: none;">Try the Project</button>
    </a>
</div>

        """, unsafe_allow_html=True)

        with st.expander("Click to view project details"):
            st.markdown("""
                **Overview**  
                This project uses YOLOv8 to detect potholes on roads in real-time. A Raspberry Pi device with a camera and GPS module is installed on a vehicle to collect data. The potholes are detected, classified by risk level, and mapped.

                **Technologies Used**  
                - YOLOv8 for object detection  
                - OpenCV for image processing  
                - GPS + Raspberry Pi  
                - Streamlit for dashboard  
                - Pandas & Plotly for analysis

                **Output**  
                - Pothole locations mapped to Riyadh streets  
                - Severity level (Low, Medium, Severe)  
                - Dashboard visualizing insights
            """)

        st.markdown("""
            <h5>Rate this project:</h5>
            <div style="font-size: 24px; color: #FFD700;">
                ★ ★ ★ ★ ★
            </div>
        """, unsafe_allow_html=True)

# الصفحة الرابعة: تواصل معي
elif selected == "Contact Me":
    st.title("Contact Me")
    st.write("Feel free to reach out via the following channels:")

    try:
        with open("cv.pdf", "rb") as file:
            cv_data = file.read()
            cv_base64 = base64.b64encode(cv_data).decode()
    except FileNotFoundError:
        cv_base64 = None
        st.warning("CV file (cv.pdf) not found. Please add it to the project directory.")

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
            <a class="btn-circle" href="{download_link}" download="cv.pdf">Download CV</a>
        </div>
    """

    st.markdown(contact_html, unsafe_allow_html=True)
