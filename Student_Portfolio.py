import streamlit as st
import time  # Import missing library

# Set the page title
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")

# Side navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Testimonials", "Contact"])

# Home section
if page == "Home":
    st.title("🎓 Student Portfolio")
    st.image("Reb.jpg", width=150, caption="Default Profile Picture")

    # Student Details
    name = st.text_input("Your Name", "NIYIMUTANZE Rebecca")
    location = st.text_input("Location", "Musanze")
    field_of_study = st.text_input("Field of Study", "Computer Science / Software Engineering Year 3")
    university = st.text_input("University", "INES-Ruhengeri")

    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🏫 {university}")

    # Download resume with error handling
    try:
        with open("resume.pdf", "rb") as file:
            resume_bytes = file.read()
            st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.error("🚨 Resume file not found. Please upload your resume named 'resume.pdf'.")

    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("Write a short description about yourself:", "I am a passionate AI student!")
    st.write(about_me)

    # Profile Customization
    if "editing_profile" not in st.session_state:
        st.session_state.editing_profile = False
    if "name" not in st.session_state:
        st.session_state.name = name
    if "location" not in st.session_state:
        st.session_state.location = location
    if "bio" not in st.session_state:
        st.session_state.bio = about_me

    if st.session_state.editing_profile:
        st.session_state.name = st.text_input("Name:", st.session_state.name)
        st.session_state.location = st.text_input("Location:", st.session_state.location)
        st.session_state.bio = st.text_area("Short introduction about myself:", st.session_state.bio)

        if st.button("Save Profile Changes"):
            st.success("✅ Profile updated successfully!")
            st.session_state.editing_profile = False  # Exit edit mode

    if st.button("Customize Profile"):
        st.session_state.editing_profile = True

    st.markdown("---")

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")

    st.subheader("⏳ Timeline of Academic & Project Milestones")
    milestones = [
        "✅ Year 2023: React Js  project completion",
        "🏆 Year 2024: Hackathon participation ",
        "💼 23/04/2025: Certified in Dion coaching center",
        "📖 Year 2025: Dissertation submission"
    ]
    for milestone in milestones:
        st.write(f" {milestone}")

    # Project Filtering System
    category = st.selectbox("Filter projects by category:", ["All", "Year 1 Project", "Year 2 Project", "Year 3 Project", "Dissertation"])

    project_data = {
        "Year 1 Project": {
            "📊 kits": {
                "type": "Individual",
                "description": "hospital management system",
                "link": "https://github.com/rebeccah-arch/rebbecca123"
            }
        },
        "Year 2 Project": {
            "🤖 Embroidery-Kits": {
                "type": "Group",
                "description": "Developed a site where kids are trained to use computers",
                "link": "https://github.com/rebeccah-arch/training"
            }
        },

        "Dissertation": {
            "🌍 A task reminder app with customizable notifications.": {
                "type": "Individual",
                "description": "",
                "link": "https://github.com/rebeccah-arch/Desertation"
            }
        }
    }

    filtered_projects = project_data.get(category, {}) if category != "All" else {k: v for cat in project_data.values() for k, v in cat.items()}

    for project, details in filtered_projects.items():
        with st.expander(project, expanded=False):
            st.write(f"**Type:** {details['type']}")
            st.write(f"**Description:** {details['description']}")
            if details.get("link"):
                st.markdown(f"[🔗 Link to Code]({details['link']})")

    st.markdown("---")

# Skills & Achievements Section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    skill_php = st.slider("PHP", 0, 100, 75)
    st.progress(skill_php)
    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    st.subheader("Certifications & Achievements")
    st.write("✔ Completed AI & ML in Business Certification")
    st.write("✔ Certified AI in Research and Course Preparation for Education")

    st.markdown("---")

# Student Testimonials Section
elif page == "Testimonials":
    st.title("🗣 Student Testimonials")

    st.subheader("💬Testimonial:")
    st.write("*Rebecca is a brilliant problem solver! Her final year project is truly innovative. – Mclement*")

    st.markdown("---")
    st.subheader("✍ Leave a Testimonial")
    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("Your Relationship", ["Classmate", "Mentor", "Teammate", "Other"])
        testimonial_message = st.text_area("Your Testimonial")

        if st.form_submit_button("Submit Testimonial") and name and testimonial_message:
            st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
            st.write(f"🗨 {testimonial_message} — {name} ({relationship})")

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Me")
    st.write("📧 Email: rebeccaniyimutanze@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/niyimutanze-rebecca-9b62b6355/)")
    st.write("📂 [GitHub](https://github.com/rebeccah-arch)")

st.sidebar.write("---")
st.sidebar.write("🔹 Made with ❤ using My Watermelon")
