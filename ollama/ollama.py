import requests
def query_ollama(prompt, model="llama3.2:1b"):
    url = "http://localhost:11434/api/generate"  # Ollama's local endpoint
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,     # Specify the model, e.g., "llama-2"
        "prompt": prompt    # Input prompt for the model
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()   # Raises an error for unsuccessful status codes
        data = response.json()        # Parse the JSON response
        return data.get("response")   # Adjust based on the actual response structure

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
result = query_ollama("What is the capital of india")
print(result)
