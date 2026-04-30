import re, os, sys

HTML_FILE = "c:/Users/Yigit Esen/Desktop/Claude/new-website/Sosyal Medya Uzmanlığı_clean.html"
ASSETS_DIR = "c:/Users/Yigit Esen/Desktop/Claude/new-website/assets"
OUTPUT_FILE = "c:/Users/Yigit Esen/Desktop/Claude/new-website/Sosyal Medya Uzmanlığı_clean.html"
CSS_FILE = os.path.join(ASSETS_DIR, "styles.css")

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

sys.stderr.write(f"Starting size: {len(content)/1024:.1f} KB\n")

# ---- Step 1: Extract unique inline styles -> CSS classes ----
style_to_class = {}
class_counter = [0]

def make_class(style_val):
    if style_val not in style_to_class:
        class_counter[0] += 1
        style_to_class[style_val] = f'is{class_counter[0]}'
    return style_to_class[style_val]

def replace_style(m):
    before_style = m.group(1)
    style_val = m.group(2)
    after_style = m.group(3)
    cls = make_class(style_val)
    full_tag = before_style + after_style
    class_match = re.search(r' class="([^"]*)"', full_tag)
    if class_match:
        old_class = class_match.group(1)
        new_full = full_tag.replace(f'class="{old_class}"', f'class="{old_class} {cls}"')
        return new_full
    else:
        return before_style + f' class="{cls}"' + after_style

content = re.sub(
    r'(<[a-zA-Z][^>]*?) style="([^"]+)"([^>]*>)',
    replace_style,
    content
)

sys.stderr.write(f"Converted {class_counter[0]} unique styles to CSS classes\n")
sys.stderr.write(f"After style extraction: {len(content)/1024:.1f} KB\n")

# ---- Step 2: Extract inline SVGs to sprite ----
svg_pattern = re.compile(r'<svg([^>]*)>(.*?)</svg>', re.DOTALL)
svg_to_id = {}
svg_counter = [0]
svg_symbols = []

def replace_svg(m):
    svg_attrs = m.group(1)
    svg_inner = m.group(2)
    key = svg_inner.strip()
    if key not in svg_to_id:
        svg_counter[0] += 1
        svg_id = f'svgsp{svg_counter[0]:04d}'
        svg_to_id[key] = svg_id
        svg_symbols.append(f'<symbol id="{svg_id}">{svg_inner}</symbol>')
    svg_id = svg_to_id[key]
    return f'<svg{svg_attrs}><use href="#{svg_id}"></use></svg>'

content = svg_pattern.sub(replace_svg, content)
sys.stderr.write(f"Found {len(svg_to_id)} unique SVGs from {svg_counter[0]} total\n")
sys.stderr.write(f"After SVG extraction: {len(content)/1024:.1f} KB\n")

if svg_symbols:
    sprite = '<svg style="display:none" xmlns="http://www.w3.org/2000/svg"><defs>' + ''.join(svg_symbols) + '</defs></svg>'
    content = content.replace('<body>', '<body>\n' + sprite + '\n', 1)
    if '<body>' not in content:
        content = re.sub(r'<body([^>]*)>', lambda mm: f'<body{mm.group(1)}>\n' + sprite + '\n', content, count=1)

sys.stderr.write(f"After adding sprite block: {len(content)/1024:.1f} KB\n")

# ---- Step 3: Append new CSS classes to styles.css ----
css_additions = []
for style_val, cls_name in sorted(style_to_class.items(), key=lambda x: x[1]):
    css_additions.append(f'.{cls_name}{{{style_val}}}')

new_css = '\n'.join(css_additions)
with open(CSS_FILE, 'a', encoding='utf-8') as f:
    f.write('\n/* Extracted inline styles */\n')
    f.write(new_css)

sys.stderr.write(f"Added {len(css_additions)} CSS rules ({len(new_css)/1024:.1f} KB) to styles.css\n")

# ---- Write output ----
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

final_size = os.path.getsize(OUTPUT_FILE)
sys.stderr.write(f"Final HTML size: {final_size:,} bytes ({final_size/1024:.1f} KB)\n")
css_size = os.path.getsize(CSS_FILE)
sys.stderr.write(f"styles.css size: {css_size:,} bytes ({css_size/1024:.1f} KB)\n")
