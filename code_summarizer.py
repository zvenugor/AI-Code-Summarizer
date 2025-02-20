import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_code(code):
    prompt = f"Summarize what the following Python code does in a few sentences:\n\n{code}\n\nSummary:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful code summarizer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Enter Python code (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    code_input = "\n".join(lines)
    summary = summarize_code(code_input)
    print("Code Summary:\n", summary)
