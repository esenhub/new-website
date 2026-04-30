import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from bs4 import BeautifulSoup, NavigableString, Tag
import re

FILE_PATH = r"C:\Users\Yigit Esen\Desktop\Claude\new-website\Sosyal Medya Uzmanlığı.html"
OUT_PATH  = r"C:\Users\Yigit Esen\Desktop\Claude\new-website\Sosyal Medya Uzmanlığı_edited.html"

# Each entry identifies a section to delete by a unique text fragment it contains.
# The script walks UP the DOM from the text node to find the appropriate section container.
TARGET_TEXTS = [
    # $23.9M proof block
    "23.9M+ in Tracked Sales",
    "Bu sistemi ilk sunduğumda",
    "İkinci seferde sistemi geliştirip",
    # paragraph below proof images
    "23.9 million from people",
    # "3. ve son kez" transition line
    "Ve şimdi, 3. ve son kez",
    # "İşe Yarıyor" testimonials block
    "İşe Yarıyor Nerede Olursan Ol",
    # Social proof reviews grid
    "Her yeni güncelleme duyurusunda müşterilerimizin",
    # 4.9/5 rating badge + supporting copy
    "4.9/5 star out of 3300",
    "Müşterilerimize gerçekten iyi bakıyoruz",
    "Senin için farklı olmayacak",
    # Booking / scheduling form section
    "Görüşme Ayarla",
    "Ekibimiz Size Yardım Etmeye Hazır",
]


def find_section_container(start_tag: Tag) -> Tag:
    """
    Walk up the tree from start_tag.
    Stop at the highest block-level element that still has ≥2 meaningful
    sibling elements — that level is the 'section' granularity we want.
    If we reach body/html first, return the last element before it.
    """
    current = start_tag
    best = start_tag

    while current.parent:
        parent = current.parent
        if parent.name in ('[document]', 'html', 'body'):
            return best
        # Count real element siblings at this level
        siblings = [s for s in parent.children if isinstance(s, Tag)]
        if len(siblings) >= 2:
            best = current   # this level looks like a real section
        current = parent

    return best


print(f"Loading {FILE_PATH} ...")
with open(FILE_PATH, "r", encoding="utf-8") as f:
    html = f.read()

print("Parsing HTML (this may take a moment for large files)...")
soup = BeautifulSoup(html, "html.parser")

removed_ids: set = set()

for target in TARGET_TEXTS:
    pattern = re.compile(re.escape(target), re.IGNORECASE)

    for text_node in soup.find_all(string=pattern):
        if not isinstance(text_node, NavigableString):
            continue

        parent = text_node.parent
        if parent is None:
            continue

        # Skip invisible blocks
        if parent.name in ("script", "style"):
            continue
        # Skip anything inside a style/script anywhere up the chain
        ancestor_names = {a.name for a in parent.parents}
        if "script" in ancestor_names or "style" in ancestor_names:
            continue

        section = find_section_container(parent)

        if id(section) not in removed_ids:
            tag_info = f"<{section.name} class='{section.get('class', '')}' id='{section.get('id', '')}'>"
            print(f"  Removing {tag_info}  ← matched: '{target}'")
            removed_ids.add(id(section))
            section.decompose()
            break   # move on to next target once one match handled

print(f"\nTotal sections removed: {len(removed_ids)}")
print(f"Writing output to {OUT_PATH} ...")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Done.")
