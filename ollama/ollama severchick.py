import requests

url = "http://localhost:11434/v/models/llama3.2:1b/generate"  # Basic URL without specific endpoint

try:
    response = requests.get(url)
    print(response.text)  # May show available routes or documentation
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
