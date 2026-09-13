import streamlit as st
import pandas as pd
import os
from datetime import date

st.title ("Student study & mood tracker")
st.write ("Welcome to your first hackathon project")

today=date.today()
name=st.text_input("What's your name: ")

##Subjects
if os.path.exists("subjects.csv"):
        st.session_state.subjects = pd.read_csv(
            "subjects.csv"
        )["Subject"].tolist()
else:
    st.session_state.subjects = [
            "CS280",
            "CS241",
            "MATH340",
            "MATH341",
            "MATH391",
            "COM312"
        ]

st.session_state.subjects.append("+ Enter a new subject")
subject = st.selectbox(
    "What subject did you study?", st.session_state.subjects)
if subject == "+ Enter a new subject":
    new_subject = st.text_input("Enter your new subject:")

    if st.button("Add Subject"):
        if new_subject:
            st.session_state.subjects.insert(-1, new_subject)

            pd.DataFrame({
                "Subject": st.session_state.subjects[:-1]
            }).to_csv("subjects.csv", index=False)

            st.success(f"{new_subject} added!")
            st.rerun()


hours=st.number_input("How many hours did you study today? ", min_value=0.0, step=0.5)

mood=st.selectbox("How are you feeling today?", ["Great!", "Not bad.", "Stressful.", "Really bad"])

if "data" not in st.session_state:
    if os.path.exists("data.csv"):
        st.session_state.data = pd.read_csv("data.csv")
    else:
        st.session_state.data = pd.DataFrame(
            columns=["Date", "Name", "Subject", "Hours", "Mood"]
        )

# 如果以前的数据没有 Subject，就自动加一列
if "Subject" not in st.session_state.data.columns:
    st.session_state.data.insert(2, "Subject", "")

# 确保 CSV 也更新
st.session_state.data.to_csv("data.csv", index=False)

    

st.subheader("📖 Previous Records")
selected_subject = st.selectbox(
    "📚 Choose a subject",
    st.session_state.data["Subject"].unique()
)
filtered_data = st.session_state.data[
    st.session_state.data["Subject"] == selected_subject
]
st.dataframe(filtered_data)
average_subject_hours = filtered_data["Hours"].mean()
st.write(
    f"📊 Average study time for {selected_subject}: "
    f" {average_subject_hours:.1f} hours"
)

##删除功能
if not st.session_state.data.empty:
    delete_index = st.selectbox(
        "Which record do you want to delete?",
        st.session_state.data.index)
    if st.button("🗑️ Delete Record"):
        st.session_state.confirm_delete = True
    if st.session_state.get("confirm_delete", False):
        st.warning("⚠️ Are you sure you want to delete this record?")
        if st.button("❌ Cancel"):
            st.session_state.confirm_delete = False

        if st.button("✅ Yes, Delete"):
            st.session_state.data = st.session_state.data.drop(index=delete_index).reset_index(drop=True)
            st.session_state.data.to_csv("data.csv", index=False)
            st.session_state.confirm_delete = False
            st.success("Record deleted!")
else:
    st.info("No records to delete.")

##删除 subject
delete_subject = st.selectbox(
    "🗑️ Which subject do you want to delete?",
    st.session_state.data["Subject"].unique()
)

if st.button("🗑️ Delete Subject"):
    st.session_state.confirm_delete_subject = True
if st.session_state.get("confirm_delete_subject", False):
    st.warning(
        f"⚠️ Are you sure you want to delete {delete_subject} "
        "and all of its study records?"
    )

    if st.button("❌ Cancel"):
        st.session_state.confirm_delete_subject = False

    if st.button("✅ Yes, Delete"):
        st.session_state.data = st.session_state.data[
        st.session_state.data["Subject"] != delete_subject
    ]
        if delete_subject in st.session_state.subjects:
            st.session_state.subjects.remove(delete_subject)

        st.session_state.data.to_csv("data.csv", index=False)

        st.session_state.confirm_delete_subject = False

        st.success(f"✅ {delete_subject} has been deleted!")
        st.rerun()

total_hours = st.session_state.data["Hours"].sum()
st.write(f"📚 Total study time: {total_hours} hours")
daily_hours = st.session_state.data.groupby("Date")["Hours"].sum()
daily_hours.index = pd.to_datetime(daily_hours.index)
average_hours=daily_hours.mean()
st.write(f"📊 Average study time per day: {average_hours:.1f} hours")
mood_counts = st.session_state.data["Mood"].value_counts()
st.line_chart(daily_hours)
st.subheader("💭 Mood Summary")
st.write(mood_counts)
st.bar_chart(mood_counts)


if st.button("START !"):
    st.session_state.data.loc[len(st.session_state.data)] = [today, name, subject, hours, mood]
    st.session_state.data.to_csv("data.csv", index=False)
    st.dataframe(st.session_state.data)

    
    st.subheader("🥰 Your daily Check-in 🥰")
    if name and mood :
        st.write("Hello "+ name+" ! 🥳")
        st.write("Welcome to your first hackathon project! 🩷")
    elif name=="":
        st.warning("Please enter a valid name!!!!! 😔")
    else:
        st.warning("please Enter your mood!!!!! 😔")

    if hours>=4:
        if mood=="Great!":
            st.success(f"🌟 Great job, {name}! You studied for {hours} hours today!")
        elif mood=="Not bad.":
            st.success(f"Good,{name}! You studied for {hours} hours, Take a break!🥰")
        elif mood=="Stressful.":
            st.info(f"It's okay {name}. You just studied for {hours} hours. Take it easy!!!😉")
        else:
            st.info(f"Don't worry {name}. You already studied for {hours} hours!!😊")
    elif hours>=2:
        if mood=="Great!":
            st.warning(f"Hi {name}, You only studied {hours} hours today. Wanna study a little bit more?? 🥲")
        elif mood=="Not bad.":
            st.warning(f"Okay {name}. You've studied {hours} hours today. Take a break and study a little bit more!! 🤓")
        elif mood=="Stressful.":
            st.warning(f"It's okay {name}. You've studied {hours} hours today. Take it easy!!! 😭")
        else:
            st.warning(f"{name}, You've studied {hours} hours today. You don't have to do everything today!! 🥺")
    else :
        if mood=="Great!":
            st.error(f"{name}, Wanna study?? You only studied {hours} hour today 📖")
        elif mood=="Not bad.":
            st.error(f"{name}, What about study a bit more!! 🫠")
        elif mood=="Stressful.":
            st.error(f"{name} Take a deep breath!!! ❤️‍🩹")
        else:
            st.error(f"It's okay {name}, try to have a good mood though!! 🤯")


