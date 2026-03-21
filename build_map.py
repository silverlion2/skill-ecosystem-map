import os
import json

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

injection_str = f"const skillContentData = {json.dumps(skill_data)}; // INJECTED_SKILL_DATA"
# Replace only if the placeholder exists
if "const skillContentData = {}; // INJECTED_SKILL_DATA" in html_content:
    html_content = html_content.replace("const skillContentData = {}; // INJECTED_SKILL_DATA", injection_str)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Success! Injected {len(skill_data)} skills into HTML.")
else:
    print("Placeholder not found in HTML.")
