#!/usr/bin/env bash
# Fetch images into assets/images/lucilles/ using curl.
set -euo pipefail
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/.. && pwd )"
MANIFEST="$ROOT/assets/images/manifest.json"
OUT="$ROOT/assets/images/lucilles"
mkdir -p "$OUT"
python3 - <<'PY' "$MANIFEST" "$OUT"
import json,sys,urllib.request,os
mf=sys.argv[1]; out=sys.argv[2]
data=json.load(open(mf))
for rec in data["images"]:
    url=rec["remote_url"]; file=rec["file"]
    print(f"Downloading {url} -> {os.path.join(out,file)}")
    try:
        urllib.request.urlretrieve(url, os.path.join(out,file))
    except Exception as e:
        print("Failed", url, e)
print("Done.")
PY
