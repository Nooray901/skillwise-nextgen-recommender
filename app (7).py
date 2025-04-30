import streamlit as st

# Banner image
st.image("banner.png", use_column_width=True)

# Header
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>SkillWise: Smart Learning Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Unlock your learning path with intelligent course suggestions based on your progress and skills.</p>", unsafe_allow_html=True)
st.markdown("–––")

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

# Course selection
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

    # Skill progress
    st.markdown("### 📊 Your Skill Progress")
    acquired_skills = course_data[selected_course]["skills"]

    # Simulate 70% progress for now (could be dynamic in the future)
    skill_progress = {skill: 70 for skill in acquired_skills}

    for skill, percent in skill_progress.items():
        st.write(f"**{skill}** – {percent}%")
        st.progress(percent)

# Footer
st.markdown(
    "<p style='text-align: center; font-size: 12px;'>Powered by <b>SkillWise</b> | Smart Learning Recommender</p>",
    unsafe_allow_html=True
)
