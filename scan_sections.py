import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from bs4 import BeautifulSoup, NavigableString, Tag

FILE_PATH = r"C:\Users\Yigit Esen\Desktop\Claude\new-website\Monetise - ORG.html"

print("Loading file (stripping base64 inline to reduce memory)...")

# Read raw and remove base64 data blobs before parsing
with open(FILE_PATH, "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

# Replace base64 payloads with a placeholder so the parser doesn't choke
html = re.sub(r'(src|srcset|style)="[^"]*base64[^"]*"', r'\1="BASE64_STRIPPED"', html)
html = re.sub(r"(src|srcset|style)='[^']*base64[^']*'", r"\1='BASE64_STRIPPED'", html)

print("Parsing HTML...")
soup = BeautifulSoup(html, "html.parser")

# Remove script/style blocks
for tag in soup.find_all(["script", "style"]):
    tag.decompose()

print("\n=== SECTION MAP ===\n")

# Walk top-level meaningful containers
TEXT_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "a", "li", "div"}
BLOCK_CONTAINERS = {"section", "article", "div", "main", "header", "footer"}

def get_text_preview(tag, max_chars=120):
    text = tag.get_text(separator=" ", strip=True)
    text = re.sub(r'\s+', ' ', text)
    return text[:max_chars] + ("..." if len(text) > max_chars else "")

def is_meaningful(tag):
    text = tag.get_text(strip=True)
    return len(text) > 20

# Find all top-level block elements under body
body = soup.find("body")
if not body:
    body = soup

count = 0
for child in body.children:
    if not isinstance(child, Tag):
        continue
    if not is_meaningful(child):
        continue
    preview = get_text_preview(child)
    if not preview.strip():
        continue
    print(f"[{count}] <{child.name}> class={child.get('class',[])} id={child.get('id','')}")
    print(f"     TEXT: {preview}")
    print()
    count += 1

print(f"\nTotal top-level sections: {count}")
