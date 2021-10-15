import requests
import os
from utils.env import get_env_var

class Azure:
  def __init__(self) -> None:
      self.url = get_env_var('AZURE_URL')
      api_key = get_env_var('AZURE_API_KEY')
      self.headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
  def predict(self, body: str) -> str:
      response = requests.post(url=self.url, headers=self.headers, data=body)

      return response.json()