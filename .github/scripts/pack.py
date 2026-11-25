"""Zip one course directory the way Schoolhouse expects: the course's files
at the root of the zip, sorted, with fixed dates so the same files always
give the same zip. Usage: pack.py <course dir> <out.zip>"""
import os
import sys
import zipfile

src, out = sys.argv[1], sys.argv[2]
paths = []
for root, dirs, files in os.walk(src):
    dirs[:] = sorted(d for d in dirs if not d.startswith("."))
    for f in files:
        if not f.startswith("."):
            paths.append(os.path.relpath(os.path.join(root, f), src).replace(os.sep, "/"))
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(paths):
        info = zipfile.ZipInfo(p, date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        with open(os.path.join(src, p), "rb") as f:
            z.writestr(info, f.read())
