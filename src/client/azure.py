import requests
from utils.env import load_env

class Azure:
  def __init__(self) -> None:
      env = load_env()
      self.url = env['AZURE_URL']
      api_key = env['AZURE_API_KEY']
      self.headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
  def predict(self, body: str) -> str:
      response = requests.post(url=self.url, headers=self.headers, data=body)

      return response.json()