from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)


html = (ROOT / "index.html").read_text()
parser = SiteParser()
parser.feed(html)

assert "Private draft" not in html
assert "candidate review pending" not in html
assert not parser.images, "The page should not depend on unattributed raster imagery"
for anchor in ("expertise", "ai-evaluation", "omics", "software", "training", "contact"):
    assert anchor in parser.ids
assert "https://www.linkedin.com/in/dilmurat-yusuf" in parser.links
for link in parser.links:
    if link.startswith("#"):
        assert link[1:] in parser.ids
    elif link.startswith("mailto:"):
        assert link == "mailto:dilmurat.yusuf@gmail.com"
    elif link == "http://rna.tbi.univie.ac.at/bcheck/":
        pass  # Published legacy service URL; no HTTPS endpoint is available.
    else:
        parsed = urlparse(link)
        assert parsed.scheme == "https" and parsed.netloc
for local in ("styles.css", "assets/SFBMR10.woff", "assets/CM-Super-README.txt"):
    assert (ROOT / local).is_file()

print(f"Portfolio checks passed: {len(parser.links)} links, {len(parser.ids)} anchors")
