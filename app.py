import streamlit as st

st.title("📚 Smart Study Planner")

st.write("Plan your daily study schedule smartly")

subjects = st.text_area(
    "Enter subjects (one per line)",
    placeholder="Maths\nPython\nOS\nEconomics"
)

hours = st.number_input(
    "How many hours can you study per day?",
    min_value=1,
    max_value=12,
    value=4
)

if st.button("Generate Study Plan"):
    subject_list = subjects.split("\n")
    subject_list = [s for s in subject_list if s.strip() != ""]

    if len(subject_list) == 0:
        st.error("Please enter at least one subject")
    else:
        per_subject = round(hours / len(subject_list), 2)

        st.success("✅ Your Study Plan")
        for sub in subject_list:
            st.write(f"📘 **{sub}** → {per_subject} hours")
