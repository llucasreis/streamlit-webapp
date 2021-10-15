import streamlit as st
import json

from client.azure import Azure

st.title("Lung Cancer Classification")

gender = st.text_input("Gender", key="Col1", value="M")
age = st.text_input("Age", key="Col2", value="1")
smoking = st.text_input("Smoking", key="Col3", value="1")
yellow_fingers = st.text_input("Yellow Fingers", key="Col4", value="1")
anxiety = st.text_input("Anxiety", key="Col5", value="1")
peer_pressure = st.text_input("Peer Presure", key="Col6", value="1")
chronic_disease = st.text_input("Chronic Disease", key="Col7", value="1")
fatigue = st.text_input("Fatigue", key="Col8", value="1")
allergy = st.text_input("Allergy", key="Col9", value="1")
wheezing = st.text_input("Wheezing", key="Col10", value="1")
alcohol_consuming = st.text_input("Alcohol Consuming", key="Col11", value="1")
coughing = st.text_input("Coughing", key="Col12", value="1")
shortness_of_breath = st.text_input("Shortness of Breath", key="Col13", value="1")
swallowing_difficulty = st.text_input("Swallowing Difficulty", key="Col14", value="1")
chest_pain = st.text_input("Chest Pain", key="Col15", value="1")

btn_predict = st.button("Realizar Previsão")

if btn_predict:
  azure = Azure()

  st_input = {
    "Inputs": {
      "input1": [
        {
          'GENDER': gender,
          'AGE': age,
          'SMOKING': smoking,
          'YELLOW_FINGERS': yellow_fingers,
          'ANXIETY': anxiety,   
          'PEER_PRESSURE': peer_pressure,   
          'CHRONIC DISEASE': chronic_disease,   
          'FATIGUE': fatigue,   
          'ALLERGY': allergy,   
          'WHEEZING': wheezing,   
          'ALCOHOL CONSUMING': alcohol_consuming,   
          'COUGHING': coughing,   
          'SHORTNESS OF BREATH': shortness_of_breath,   
          'SWALLOWING DIFFICULTY': swallowing_difficulty,   
          'CHEST PAIN': chest_pain,   
          'LUNG_CANCER': "",
        }
      ]
    },
    "GlobalParameters": {
    }
  }

  data = str.encode(json.dumps(st_input))

  try:
    response = azure.predict(data)

    print(response)
    st.markdown(response)
  except Exception as e:
    print("Exception: ", e)