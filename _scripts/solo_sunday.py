"""
Reads https://www.solosunday.com/upcoming-shows.html and writes the next
upcoming show to _data/solo_sunday.yml. Runs automatically on GitHub every
morning (see .github/workflows/build.yml). If anything goes wrong, it leaves
the existing _data/solo_sunday.yml alone, so the site never breaks.
Standard library only.
"""
import datetime as dt
import html
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

URL = "https://www.solosunday.com/upcoming-shows.html"
OUT = "_data/solo_sunday.yml"

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], 1)}
DATE_RE = re.compile(r"(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})", re.I)
TIME_RE = re.compile(r"(\d{1,2}(?::\d{2})?\s*[ap]\.?m\.?)", re.I)


class Flattener(HTMLParser):
    """Turns the page into a list of lines; each line remembers images and links seen."""
    BREAKS = {"br", "p", "div", "td", "tr", "h1", "h2", "h3", "h4", "li", "table"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []  # ("text", str) | ("img", src) | ("link", href, text) | ("br",)
        self._a = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.BREAKS:
            self.items.append(("br",))
        if tag == "img" and a.get("src"):
            self.items.append(("img", a["src"]))
        if tag == "a":
            self._a = [a.get("href", ""), ""]

    def handle_endtag(self, tag):
        if tag == "a" and self._a:
            self.items.append(("link", self._a[0], self._a[1].strip()))
            self._a = None
        if tag in self.BREAKS:
            self.items.append(("br",))

    def handle_data(self, data):
        if self._a is not None:
            self._a[1] += data
        self.items.append(("text", data))


def lines_from(items):
    lines, cur = [], {"text": "", "imgs": [], "links": []}
    for it in items:
        if it[0] == "br":
            lines.append(cur)
            cur = {"text": "", "imgs": [], "links": []}
        elif it[0] == "text":
            cur["text"] += it[1]
        elif it[0] == "img":
            cur["imgs"].append(it[1])
        elif it[0] == "link":
            cur["links"].append((it[1], it[2]))
    lines.append(cur)
    for l in lines:
        l["text"] = re.sub(r"\s+", " ", l["text"].replace("\u200b", "")).strip()
    return lines


def absolute(src):
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("/"):
        return "https://www.solosunday.com" + src
    return src


def find_shows(lines):
    starts = [i for i, l in enumerate(lines) if re.match(r"^by\s+\S", l["text"], re.I)]
    shows = []
    for n, i in enumerate(starts):
        t = i - 1
        while t >= 0 and not lines[t]["text"]:
            t -= 1
        if t < 0:
            continue
        seg_start = max(t - 6, starts[n - 1] + 1 if n else 0)
        seg_end = starts[n + 1] - 1 if n + 1 < len(starts) else len(lines)
        seg = lines[seg_start:seg_end]
        details = lines[i + 1:i + 6]
        date = time = None
        for l in details:
            m = DATE_RE.search(l["text"])
            if m and not date:
                date = dt.date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2)))
            tm = TIME_RE.search(l["text"])
            if tm and not time:
                time = tm.group(1).upper().replace(".", "").replace("  ", " ")
        imgs = [absolute(s) for l in seg for s in l["imgs"] if "/uploads/" in s]
        link = next((h for l in lines[i:seg_end] for h, txt in l["links"] if "ticket" in txt.lower()), None)
        blurb = ""
        for l in lines[i + 1:seg_end]:
            if len(l["text"]) > 80:
                blurb = l["text"]
                break
        shows.append({
            "title": lines[t]["text"].strip("*! ").strip() + ("!" if lines[t]["text"].rstrip().endswith("!") else ""),
            "by": re.sub(r"^by\s+", "", lines[i]["text"], flags=re.I).strip(),
            "date": date.isoformat() if date else None,
            "time": time,
            "image": imgs[0] if imgs else None,
            "link": absolute(link) if link else None,
            "blurb": blurb,
        })
    return shows


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "laurenkee.com site build"})
    page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    p = Flattener()
    p.feed(page)
    shows = find_shows(lines_from(p.items))
    today = dt.date.today().isoformat()
    upcoming = [s for s in shows if s["date"] and s["date"] >= today]
    if not upcoming:
        print("No dated upcoming Solo Sunday show found; leaving existing data alone.")
        return 1
    nxt = sorted(upcoming, key=lambda s: s["date"])[0]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# Written automatically from solosunday.com each morning.\n")
        f.write("# You can edit it by hand too; the next automatic run will replace it.\n")
        for k in ["title", "by", "date", "time", "image", "link", "blurb"]:
            if nxt.get(k):
                f.write(f"{k}: {json.dumps(nxt[k], ensure_ascii=False)}\n")
    print("Next Solo Sunday show:", nxt["title"], nxt["date"])
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # never break the site build
        print("Solo Sunday check failed:", e)
        sys.exit(0)
