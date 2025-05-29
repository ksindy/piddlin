import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a developer assistant working on a science education site using MkDocs with the Material theme. "
                "You write and modify Markdown content and YAML config directly."
            )
        },
        {
            "role": "user",
            "content": """Please make the following changes to my MkDocs site:

1. Create or update `docs/activities/my-activity.md` with:
   - A clean, professional introduction to "My Activity"
   - An embedded PDF viewer for `files/my-activity.pdf`
   - Download links for both `my-activity.pdf` and `my-activity-cutouts.pdf`

2. Edit `mkdocs.yml`:
   - Under `nav`, add a new section called "Activities" with a link to this page

3. Enhance the site visually:
   - Use the Material for MkDocs theme
   - Set a custom primary and accent color
   - Enable navigation tabs and instant loading
   - Add a Google Font for a modern look

Return the updated `my-activity.md` content and the full updated `mkdocs.yml`.
Assume the files are already stored in `docs/files/`.
"""
        }
    ]
)

print(response.choices[0].message.content)
