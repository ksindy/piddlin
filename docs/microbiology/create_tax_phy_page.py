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
                "You are a developer assistant helping to build a clean, professional, and educational "
                "MkDocs site using the Material for MkDocs theme."
            )
        },
        {
            "role": "user",
            "content": """I have a PDF-based activity called "My Activity" with a cutouts sheet. Please:
1. Create a new Markdown file called `docs/activities/my-activity.md` that:
   - Has a sleek, clean introduction to the activity
   - Embeds the PDF located at `docs/files/my-activity.pdf` for in-browser viewing
   - Provides download links for `my-activity.pdf` and `my-activity-cutouts.pdf`
2. Update the `mkdocs.yml` to include this under a new "Activities" section
3. Suggest CSS or Material theme settings to make the page look more visually polished and modern
"""
        }
    ]
)

print(response.choices[0].message.content)
