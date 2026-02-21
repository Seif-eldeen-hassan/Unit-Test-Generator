import os
from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()

def generate_unit_tests(cleaned_code: str):
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN"),
    )
    
    system_instruction = (
        "You are a Python unit testing expert. "
        "Generate comprehensive unit tests using the 'unittest' library. "
        "CRITICAL RULES:\n"
        "1. Output ONLY the raw Python code.\n"
        "2. Do NOT use markdown code blocks.\n"
        "3. Do NOT provide any explanation, intro, or outro text.\n"
        "4. Output must be ready to run as a .py file."
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Generate tests for this function:\n\n{cleaned_code}"}
        ],
        model="gpt-4o", 
        temperature=0.0
    )
    
    return response.choices[0].message.content.strip()