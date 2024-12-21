# import ollama

# class OllamaAI:
#     def __init__(self, model="gpt-3.5"):
#         self.agent = ollama.query(model=model)

#     def analyze_diff(self, diff_text):
#         try:
#             response = self.agent.query(diff_text)
#             return response
#         except Exception as e:
#             return str(e)



import requests

def analyze_diff_with_ollama(diff):
    url = "tg"
    payload = {"diff": diff}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()
