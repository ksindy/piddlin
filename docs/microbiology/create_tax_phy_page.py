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
                "You are a developer assistant with write access to a MkDocs project using the Material theme. "
                "Make all edits directly to existing files or create new ones as needed."
            )
        },
        {
            "role": "user",
            "content": """Integrate the following changes into my MkDocs site:

1. Create a new file at `docs/activities/my-activity.md` with:
   - A professional introduction to "My Activity"
   - An embedded PDF viewer for `microbiology/files/my-activity.pdf`
   - Download links for both `my-activity.pdf` and `my-activity-cutouts.pdf` stored in `docs/microbiology/files/`

2. Update `mkdocs.yml`:
   - Add this new page under a section called "Activities"

3. Apply a sleek professional look:
   - Use the Material for MkDocs theme
   - Set the primary color to indigo and accent to teal
   - Use the Roboto font
   - Enable `navigation.tabs` and `navigation.instant`

Make all changes directly and return the full contents of the modified files:
- `docs/activities/my-activity.md`
- `mkdocs.yml`
"""
        }
    ]
)

print(response.choices[0].message.content)
