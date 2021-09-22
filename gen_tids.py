import sys
import json
from datetime import datetime
from pathlib import Path

PLComp = '''tags: %s
title: PLComp
type: text/vnd.tiddlywiki

<<list-links "[tag[published]reverse[]]">>
'''

Message = '''tags: published %s
title: %04d-%02d-%02d %s
type: text/x-markdown

Автор: %s

%s
'''

def get_all_tags(entries):
    tags = set()
    for entry in entries:
        tags |= set(entry["tags"])
    return tags


def get_title(text, limit=60):
    pos = min(text.find('.'), text.find('\n'))
    if pos < limit:
        title = text[:pos]
    else:
        text = text[:limit]
        title = text[:text.rfind(' ')] + "..."
    return title.replace("*", "")


entries = json.loads(Path(sys.argv[1]).read_text(encoding="utf8"))

Path("PLComp.tid").write_text(PLComp % " ".join(get_all_tags(entries)))

for entry in entries:
    tags = " ".join(entry["tags"])
    d = datetime.fromisoformat(entry["date"])
    title = get_title(entry["text"])
    author = entry["author"]
    text = Message % (tags, d.year, d.month, d.day, title, author,
        entry["text"])
    Path("%d.tid" % entry["id"]).write_text(text, encoding="utf8")
