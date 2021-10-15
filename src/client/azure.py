import requests

class Azure:
  def __init__(self) -> None:
      self.url = ''
      api_key = ''
      self.headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
  def predict(self, body: str) -> str:
      response = requests.post(url=self.url, headers=self.headers, data=body)

      return response.json()