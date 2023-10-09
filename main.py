import cv2
import streamlit as st
import time

st.title("Motion Detector")
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        current_time = time.time()
        current_time_struct = time.localtime(current_time)
        day = current_time_struct.tm_wday
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_name = days_of_week[day]
        current_time_string = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
        formated_day = f"{day_name}"
        formated_time = f"{current_time_string}"
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=formated_day,  org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=formated_time,  org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)        

        streamlit_image.image(frame)