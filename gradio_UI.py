#Ollama call 
import gradio as gr
from scraper import Website
from prompts import system_prompt, user_prompt
import requests

def summarize_website(company_name, url):
    try:
        site = Website(url)
        prompt = user_prompt(site)

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "system": system_prompt(),
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()["response"]
        return f"## {site.title}\n\n{result}"

    except Exception as e:
        return f"❌ Error: {str(e)}"

iface = gr.Interface(
    fn=summarize_website,
    inputs=[gr.Textbox(label="Company Name"), gr.Textbox(label="Website URL")],
    outputs="markdown",
    title="Web Scraper & LLM Summarizer"
)

if __name__ == "__main__":
    iface.launch()
