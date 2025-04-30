
import streamlit as st

# Set up the page
st.set_page_config(page_title="SkillWise: NextGen Course Recommender", layout="wide")

# App title and intro
st.markdown("<h1 style='text-align: center; color: green;'>SkillWise: Your Personalized Course Guide</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Finish one course, unlock the next. Smart, skill-based recommendations await.</p>", unsafe_allow_html=True)
st.markdown("---")

# User Input
st.sidebar.header("📚 Your Course Tracker")
completed_course = st.sidebar.selectbox("Select the course you've completed:", [
    "Python for Beginners", 
    "Intro to SQL", 
    "Data Analysis with Pandas"
])

# Skill tagging logic
course_skills = {
    "Python for Beginners": ["Python", "Programming Basics"],
    "Intro to SQL": ["SQL", "Databases"],
    "Data Analysis with Pandas": ["Python", "Data Analysis"]
}

recommendations = {
    "Python": ["Intermediate Python", "Python Projects"],
    "Programming Basics": ["Data Structures", "Object-Oriented Programming"],
    "SQL": ["Advanced SQL", "Database Design"],
    "Databases": ["NoSQL Basics", "Data Warehousing"],
    "Data Analysis": ["Data Visualization", "Machine Learning Intro"]
}

# Generate recommendations
st.subheader("🔍 Based on Your Skills, We Recommend:")
skills = course_skills.get(completed_course, [])
rec_courses = []
for skill in skills:
    rec_courses.extend(recommendations.get(skill, []))

# Remove duplicates while preserving order
seen = set()
unique_courses = [x for x in rec_courses if not (x in seen or seen.add(x))]

# Display recommendations
for course in unique_courses:
    st.markdown(f"- {course}")
