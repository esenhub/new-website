import re
import base64
import os

HTML_FILE = "Sosyal Medya Uzmanlığı.html"
ASSETS_DIR = "assets"
OUTPUT_FILE = "Sosyal Medya Uzmanlığı_clean.html"

os.makedirs(ASSETS_DIR, exist_ok=True)

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Match src="data:image/TYPE;base64,DATA" or url(data:image/TYPE;base64,DATA)
pattern = re.compile(r'data:(image/[a-zA-Z+]+);base64,([A-Za-z0-9+/=]+)')

counter = [0]
replacement_map = {}

def replace_match(m):
    mime = m.group(1)          # e.g. image/png
    data = m.group(2)
    ext = mime.split("/")[1].replace("jpeg", "jpg").split("+")[0]
    key = m.group(0)
    if key in replacement_map:
        return f"assets/{replacement_map[key]}"
    counter[0] += 1
    filename = f"image{counter[0]:04d}.{ext}"
    replacement_map[key] = filename
    with open(os.path.join(ASSETS_DIR, filename), "wb") as imgf:
        imgf.write(base64.b64decode(data))
    return f"assets/{filename}"

clean_html = pattern.sub(replace_match, html)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(clean_html)

print(f"Done. Extracted {counter[0]} image(s) to '{ASSETS_DIR}/'")
print(f"Clean HTML saved as '{OUTPUT_FILE}'")
original_kb = os.path.getsize(HTML_FILE) // 1024
clean_kb = os.path.getsize(OUTPUT_FILE) // 1024
print(f"Original: {original_kb:,} KB  →  Clean: {clean_kb:,} KB")
