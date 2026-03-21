import os
import json
import re

skills_dir = r"C:\Users\T480S\.gemini\antigravity\.skills"
html_path = r"C:\Users\T480S\skill mapping\skill_map.html"

skill_data = {}

for skill_id in os.listdir(skills_dir):
    skill_path = os.path.join(skills_dir, skill_id, "SKILL.md")
    if os.path.isfile(skill_path):
        with open(skill_path, 'r', encoding='utf-8') as f:
            skill_data[skill_id] = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

json_str = json.dumps(skill_data).replace("</", "<\\/")
injection_str = f"const skillContentData = {json_str}; // INJECTED_SKILL_DATA"

html_content = re.sub(r"const skillContentData = .*?; // INJECTED_SKILL_DATA", lambda m: injection_str, html_content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Fixed and injected {len(skill_data)} skills into HTML.")
