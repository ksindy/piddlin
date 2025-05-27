import os

folders = {
    "microbiology": ["lectures.md", "lab_prep.md"],
    "lab_management": ["checklists.md", "tools.md"],
    "teaching_toolkit": ["printables.md", "course_outlines.md"],
    "": ["about.md"]
}

for folder, files in folders.items():
    path = os.path.join("docs", folder)
    os.makedirs(path, exist_ok=True)
    for f in files:
        with open(os.path.join(path, f), "w") as file:
            file.write(f"# {f.replace('.md', '').replace('_', ' ').title()}")

