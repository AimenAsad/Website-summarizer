import requests

def test_ollama_connection():
    model = "llama3"
    prompt = "Test connection with Ollama"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt}
    )
    print(response.json()["response"])

if __name__ == "__main__":
    test_ollama_connection()
