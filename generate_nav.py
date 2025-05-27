import os
from openai import OpenAI

# Use API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who writes clean YAML config for MkDocs."
        },
        {
            "role": "user",
            "content": """Create a mkdocs.yml nav for a biology educator website with the following sections:
- Microbiology (with lectures and lab prep)
- Lab Management (checklists, tools)
- Teaching Toolkit (printables, course outlines)
- About page"""
        }
    ]
)

print(response.choices[0].message.content)

