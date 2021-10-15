import requests
import os

class Azure:
  def __init__(self) -> None:
      self.url = os.getenv('AZURE_URL')
      api_key = os.getenv('AZURE_API_KEY')
      self.headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
  def predict(self, body: str) -> str:
      response = requests.post(url=self.url, headers=self.headers, data=body)

      return response.json()