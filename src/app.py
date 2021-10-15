import streamlit as st

from client.azure import Azure

st.title("Streamlit WebApp")

btn_predict = st.button("Realizar Previsão")

if btn_predict:
  azure = Azure()

  data = ""

  try:
    response = azure.predict(data)

    print(response)
    st.markdown(response)
  except Exception as e:
    print("Exception: ", e)