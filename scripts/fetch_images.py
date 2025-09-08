#!/usr/bin/env python3
"""
Fetch images listed in assets/images/manifest.json into assets/images/lucilles/.
Run this on your own machine with internet access (and appropriate rights).
"""
import os, json, pathlib, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
manifest_path = ROOT / "assets" / "images" / "manifest.json"
out_dir = ROOT / "assets" / "images" / "lucilles"
out_dir.mkdir(parents=True, exist_ok=True)

data = json.loads(manifest_path.read_text(encoding="utf-8"))
for rec in data.get("images", []):
    url = rec["remote_url"]
    fname = rec["file"]
    dest = out_dir / fname
    try:
        print(f"Downloading {url} -> {dest}")
        urllib.request.urlretrieve(url, dest)
    except Exception as e:
        print(f"Failed: {url} ({e})")
print("Done.")
