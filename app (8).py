# NOTE: This environment does not support Streamlit.
# The code below is designed to be used in a local Python environment where Streamlit is installed.
# You can run it using: `streamlit run app.py` after installing Streamlit via `pip install streamlit`

try:
    import streamlit as st

    # ✅ Set page config FIRST
    st.set_page_config(page_title="SkillWise NextGen Recommender", layout="wide")

    # ✅ Display the banner
    st.image("banner.png", use_container_width=True)

    # Header (for screen readers or fallback)
    st.markdown("<h1 style='text-align: center; color: #2E8B57;'>SkillWise: Smart Learning Recommender</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Unlock your learning path with intelligent course suggestions based on your progress and skills.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Sample course progress database
    course_data = {
        "Python for Beginners": {
            "skills": ["Python Basics", "Logic", "Variables"],
            "next_courses": ["Data Analysis with Pandas", "Intro to SQL", "Python Projects"]
        },
        "Data Analysis with Pandas": {
            "skills": ["Pandas", "Data Wrangling"],
            "next_courses": ["Data Visualization", "Intermediate Python", "Statistics 101"]
        },
        "Intro to SQL": {
            "skills": ["SQL Basics", "Databases"],
            "next_courses": ["Advanced SQL", "Database Design", "SQL for Data Science"]
        }
    }

    all_courses = list(course_data.keys())
    selected_course = st.selectbox("✅ Select a course you've completed:", all_courses)

    if selected_course:
        st.success(f"Course completed: {selected_course}")

        next_courses = course_data[selected_course]["next_courses"]
        st.markdown("### 🎯 Recommended Next Courses:")
        for course in next_courses:
            st.markdown(f"- {course}")

        st.markdown("### 🔍 Why these courses?")
        st.markdown("* These are selected based on the skills you've built so far.")
        st.markdown("* They align with your progress and open new opportunities.")

        st.markdown("### 📊 Your Skill Progress")
        acquired_skills = course_data[selected_course]["skills"]
        skill_progress = {}
        for skill in acquired_skills:
            skill_progress[skill] = 70  # Simulated percentage

        for skill, percent in skill_progress.items():
            st.write(f"**{skill}** – {percent}%")
            st.progress(percent)

    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; font-size: 12px;'>Powered by <b>SkillWise</b> | Smart Learning Recommender</p>",
        unsafe_allow_html=True
    )

except ModuleNotFoundError:
    print("Streamlit is not installed in this environment. Please install it locally with 'pip install streamlit' and run the app using 'streamlit run app.py'")
