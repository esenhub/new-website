import re, os, sys

HTML_FILE = "c:/Users/Yigit Esen/Desktop/Claude/new-website/Sosyal Medya Uzmanlığı_clean.html"
ASSETS_DIR = "c:/Users/Yigit Esen/Desktop/Claude/new-website/assets"
OUTPUT_FILE = HTML_FILE

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

sys.stderr.write(f"Starting: {len(content)/1024:.1f} KB\n")

before = len(content)

# ---- Strip non-display data-framer-* attributes ----
# data-framer-name: internal editor names
content = re.sub(r' data-framer-name="[^"]*"', '', content)
# data-framer-background-image-wrapper: layout hint
content = re.sub(r' data-framer-background-image-wrapper="[^"]*"', '', content)
# data-framer-component-type: internal type
content = re.sub(r' data-framer-component-type="[^"]*"', '', content)
# data-framer-appear-id: animation identifier
content = re.sub(r' data-framer-appear-id="[^"]*"', '', content)
# metadata attributes
content = re.sub(r' data-framer-hydrate-v2="[^"]*"', '', content)
content = re.sub(r' data-framer-ssr-released-at="[^"]*"', '', content)
content = re.sub(r' data-framer-page-optimized-at="[^"]*"', '', content)
content = re.sub(r' data-framer-generated-page(?:="[^"]*")?', '', content)
content = re.sub(r' data-framer-root(?:="[^"]*")?', '', content)
content = re.sub(r' data-framer-bundle="[^"]*"', '', content)

framer_saved = before - len(content)
sys.stderr.write(f"Stripped data-framer-*: -{framer_saved/1024:.1f} KB\n")

# ---- Strip other non-essential data attributes ----
before2 = len(content)
content = re.sub(r' data-styles-preset="[^"]*"', '', content)
content = re.sub(r' data-border="[^"]*"', '', content)
content = re.sub(r' data-highlight="[^"]*"', '', content)
content = re.sub(r' data-text-fill="[^"]*"', '', content)
content = re.sub(r' data-reset="[^"]*"', '', content)
content = re.sub(r' data-new-gr-c-s-check-loaded="[^"]*"', '', content)
content = re.sub(r' data-gr-ext-installed(?:="[^"]*")?', '', content)
content = re.sub(r' data-no-nt(?:="[^"]*")?', '', content)
# Remove empty data-url and data-id if they appear to be tracking
content = re.sub(r' data-id="CVESG6BC[^"]*"', '', content)
content = re.sub(r' data-fid="[^"]*"', '', content)

other_saved = before2 - len(content)
sys.stderr.write(f"Stripped other data-*: -{other_saved/1024:.1f} KB\n")

# ---- Strip aria-hidden (not essential for display) ----
before3 = len(content)
content = re.sub(r' aria-hidden="[^"]*"', '', content)
aria_saved = before3 - len(content)
sys.stderr.write(f"Stripped aria-hidden: -{aria_saved/1024:.1f} KB\n")

# ---- Extract SVG sprite to external file ----
before4 = len(content)
sprite_match = re.search(r'<svg style="display:none" xmlns="http://www.w3.org/2000/svg"><defs>(.*?)</defs></svg>', content, re.DOTALL)
if sprite_match:
    sprite_content = sprite_match.group(1)
    sprite_svg = '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg"><defs>' + sprite_content + '</defs></svg>'
    sprite_path = os.path.join(ASSETS_DIR, 'sprite.svg')
    with open(sprite_path, 'w', encoding='utf-8') as f:
        f.write(sprite_svg)
    # Replace inline sprite with empty reference (browser will load it on demand)
    content = content.replace(sprite_match.group(0), '', 1)
    # Update <use href="#svgXXXX"> to point to external file
    content = re.sub(r'href="#(svgsp\d+)"', r'href="assets/sprite.svg#\1"', content)
    svg_saved = before4 - len(content)
    sys.stderr.write(f"Extracted SVG sprite to assets/sprite.svg: -{svg_saved/1024:.1f} KB (sprite file: {len(sprite_svg)/1024:.1f} KB)\n")

# ---- Strip download_date meta tag ----
content = re.sub(r'<meta name="download_date"[^>]+/>', '', content)

# ---- Collapse multiple spaces/newlines in tag attributes ----
# Cleanup empty attribute slots left by stripping
content = re.sub(r'  +', ' ', content)

sys.stderr.write(f"After all stripping: {len(content)/1024:.1f} KB\n")

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

final_size = os.path.getsize(OUTPUT_FILE)
sys.stderr.write(f"Final HTML: {final_size:,} bytes ({final_size/1024:.1f} KB)\n")
total_saved = (7247566 - final_size)
sys.stderr.write(f"Total saved from original: {total_saved/1024/1024:.1f} MB ({total_saved*100//7247566}%)\n")
