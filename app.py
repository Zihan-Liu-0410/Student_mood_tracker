import streamlit as st
st.title ("Student study & mood tracker")
st.write ("Welcome to your first hackathon project")

name=st.text_input("What's your name: ")
hours=st.number_input("How many hours did you study today? ", min_value=0.0, step=0.5)

mood=st.selectbox("How are you feeling today?", ["Great!", "Not bad.", "Stressful.", "Really bad"])

if st.button("START !"):
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

