import streamlit as st
from streamlit.elements.alert import AlertMixin
import json

from client.azure import Azure

st.title("Lung Cancer Prediction")
st.markdown("Este é um Data App para Diagnóstico preditivo de Câncer de Pulmão")
st.markdown("Desenvolvido pelos alunos: Andrea Mendonça, Francisco Marcelo, Lucas Pereira e Marcos Wenneton " \
            "para a discplina de Infraestrutura em Nuvem para Projetos com Ciência dos Dados do curso de Pós-Graduação "\
            "em Ciência de Dados da Universidade do Estado do Amazonas - UEA.")

gender = st.selectbox("Gênero", ('Feminino', 'Masculino'), key="gender",)
age = st.text_input("Idade", key="age", value="1")
smoking = st.checkbox("Fumante", key="smoking")
yellow_fingers = st.checkbox("Dedos amarelados", key="yellow_fingers")
anxiety = st.checkbox("Ansiedade", key="anxiety")
peer_pressure = st.checkbox("Pressão dos pares", key="peer_pressure")
chronic_disease = st.checkbox("Doença Crônica", key="chronic_disease")
fatigue = st.checkbox("Fadiga", key="fatigue")
allergy = st.checkbox("Alergia", key="allergy")
wheezing = st.checkbox("Respiração Ofegante", key="wheezing")
alcohol_consuming = st.checkbox("Toma bebida alcólica", key="alcohol_consuming")
coughing = st.checkbox("Tosse", key="coughing")
shortness_of_breath = st.checkbox("Falta de ar", key="shortness_of_breath")
swallowing_difficulty = st.checkbox("Dificuldade para engolor", key="swallowing_difficulty")
chest_pain = st.checkbox("Dores no peito", key="chest_pain")

btn_predict = st.button("Realizar Previsão")

def normalize_option(option):
  if option:
    return 2
  else:
    return 1

def normalize_gender(option):
  if option == 'Feminino':
    return 1
  else:
    return 2

def show_results(response):
  result = response['Results']['output1'][0]['Scored Labels']
  if result == 'NO':
    st.success("NEGATIVO: Aparentemente está tudo bem com você :)")
  elif result == 'YES':
    st.error("POSITIVO: Talvez seja bom consultar um médico :|")

  st.warning("ATENÇÃO! O resultado acima é apenas um experimento acadêmico, procure um médico caso não esteja se sentido bem! :)")


if btn_predict:
  azure = Azure()

  st_input = {
      "Inputs": {
          "input1":
          [
              {
                  'GENDER': gender,
                  'AGE': age,
                  'SMOKING': normalize_option(smoking),
                  'YELLOW_FINGERS': normalize_option(yellow_fingers),
                  'ANXIETY': normalize_option(anxiety),
                  'PEER_PRESSURE': normalize_option(peer_pressure),
                  'CHRONIC DISEASE': normalize_option(chronic_disease),
                  'FATIGUE': normalize_option(fatigue),
                  'ALLERGY': normalize_option(allergy),
                  'WHEEZING': normalize_option(wheezing),
                  'ALCOHOL CONSUMING': normalize_option(alcohol_consuming),
                  'COUGHING': normalize_option(coughing),
                  'SHORTNESS OF BREATH': normalize_option(shortness_of_breath),
                  'SWALLOWING DIFFICULTY': normalize_option(swallowing_difficulty),
                  'CHEST PAIN': normalize_option(chest_pain),
                  'LUNG_CANCER': "",
              }
          ],
      },
      "GlobalParameters":  {
      }
  }

  data = str.encode(json.dumps(st_input))

  try:
    response = azure.predict(data)

    print(response)
    #st.markdown(response)
    show_results(response)
  except Exception as e:
    print("Exception: ", e)
