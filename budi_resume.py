from pathlib import Path
import streamlit as st
from PIL import Image

# ---- PATH SETTINGS ----
current_dir = Path(__name__).parent if '__file__' in locals() else Path.cwd() 
css_file = current_dir/ "styles" / "main.css"
cv_file = current_dir/ "assets" / "myCV.pdf"
my_profile = current_dir/ "assets" / "profile.jpg"

# ---- GENERAL SETTINGS ----
PAGE_TITLE = "DIGITAL CV | SETIA BUDI SUMANDRA"
PAGE_ICON = ':wave:'
NAME = "SETIA BUDI SUMANDRA"
DESCRIPTION = "Junior Data Scientist, build descriptive and predictive analysis to support decision-making"
EMAIL = 'budisumandra325@gmail.com'
SOCIAL_MEDIA = {
    "Medium": "https://medium.com/@budisumandra",
    "LinkedIn": "https://www.linkedin.com/in/setia-budi-sumandra-42b992213/",
    "GitHub": "https://github.com/budisumandra"
}
PROJECTS = {
    "🏆 Water Potability Prediction": "https://budisumandra-water-potability-prediction-app-625p0w.streamlit.app/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with st.sidebar:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVTP67OXr54opMcPmQHDBCEQ6PIwzgufELfg&usqp=CAU')
    st.sidebar.subheader('CHOOSE MENU')
    menus = st.radio('',['Profile','project_examples'])
    st.info('THANK YOU')

# ---- LOAD CSS, PDF, AND PROFILE PICT ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

if menus == 'Profile':
    with open(cv_file, 'rb') as cv:
        PDFbyte = cv.read()
    profile_pic = Image.open(my_profile)

    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=cv_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # ---- SOCIAL MEDIA SECTION ----
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[i].write(f"[{platform}]({link})")

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader('Experience and Qualifications')
    st.write(
        """
    - ✔️ 7 Years expereince extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge in Python and Excel
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - 📊 Data Visulization: PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees
    - 🗄️ Databases: Postgres, MongoDB, MySQL
    """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Senior Data Analyst | Ross Industries**")
    st.write("02/2020 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► Redesigned data model through iterations that improved predictions by 12%
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )


    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

else:
    pass