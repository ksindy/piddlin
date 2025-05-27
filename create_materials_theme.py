import os
import yaml

# Paths
base_path ="/home/karlysindy/science-site"  # Update if needed
mkdocs_path = os.path.join(base_path, "mkdocs.yml")
index_md_path = os.path.join(base_path, "docs/index.md")

# 1. Update mkdocs.yml theme to 'material'
with open(mkdocs_path, 'r') as file:
    config = yaml.safe_load(file)

config['theme'] = {
    'name': 'material',
    'palette': [
        {
            'scheme': 'default',
            'primary': 'indigo',
            'accent': 'indigo'
        }
    ],
    'font': {
        'text': 'Roboto',
        'code': 'Roboto Mono'
    },
    'features': [
        'navigation.tabs',
        'navigation.instant',
        'search.highlight',
        'search.suggest'
    ]
}

with open(mkdocs_path, 'w') as file:
    yaml.dump(config, file, sort_keys=False)

# 2. Update docs/index.md with sleek intro content
sleek_homepage = """# 👋 Welcome to Biology Educator Hub

This site provides:
- 🧫 Microbiology teaching resources
- 🧪 Lab management tools
- 🧠 Workflow and planning templates

> Created by Karly Sindy, molecular biologist, educator, and lab manager.

!!! note
    This is a living site—more content is added regularly!
"""

with open(index_md_path, 'w') as file:
    file.write(sleek_homepage)

print("✅ mkdocs.yml updated with Material theme and features.")
print("✅ docs/index.md updated with stylish homepage content.")

