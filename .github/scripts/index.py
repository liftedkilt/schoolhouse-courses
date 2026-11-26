"""Write courses.json, the index Schoolhouse reads to browse this repository's
courses: one entry per course (the version on main), with its release zip's
link and SHA-256. Usage: index.py <repo owner/name> <dir with the zips> <out>

The zips directory holds <id>-<version>.zip for every course (downloaded
from, or just uploaded to, its release), so the hash is of the very file a
Schoolhouse server will download."""
import datetime
import glob
import hashlib
import json
import os
import sys

import yaml

repo, zips, out = sys.argv[1], sys.argv[2], sys.argv[3]
courses = []
for manifest in sorted(glob.glob("*/course.yaml")):
    d = os.path.dirname(manifest)
    m = yaml.safe_load(open(manifest))
    cid, version = m["id"], str(m["version"])
    live = 0
    units = []
    for u in m.get("units", []):
        units.append(u["name"])
        sk = yaml.safe_load(open(os.path.join(d, u["file"]))) or {}
        live += sum(1 for s in sk.get("skills", []) if s.get("status") == "live")
    needs = []

    def walk(rule):
        if isinstance(rule, dict):
            if rule.get("course") and rule["course"] not in needs:
                needs.append(rule["course"])
            for k in ("all", "any"):
                for r in rule.get(k, []):
                    walk(r)

    walk(m.get("requires") or {})
    zpath = os.path.join(zips, f"{cid}-{version}.zip")
    data = open(zpath, "rb").read()
    tag = f"course-{cid}-v{version}"
    courses.append({
        "id": cid,
        "version": version,
        "title": m.get("title", cid),
        "summary": m.get("summary", ""),
        "ages": (m.get("audience") or {}).get("ages", ""),
        "units": units,
        "skills": live,
        "requires": needs,
        "url": f"https://github.com/{repo}/releases/download/{tag}/{cid}-{version}.zip",
        "sha256": hashlib.sha256(data).hexdigest(),
        "size": len(data),
    })
index = {
    "format": 1,
    "name": "Schoolhouse courses",
    "home": f"https://github.com/{repo}",
    "updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "courses": courses,
}
with open(out, "w") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"{len(courses)} courses in {out}")
