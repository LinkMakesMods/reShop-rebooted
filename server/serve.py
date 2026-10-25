#!/usr/bin/env python3
"""
Tiny listings server for reShop. Serves YOUR OWN homebrew (.cia / .3dsx) to your 3DS.

Put files in ./apps/ :
    MyApp.cia            the installable (or MyApp.3dsx)
    MyApp.png            optional 64x64 icon
    MyApp.json           optional {"name": "...", "desc": "..."}

Run:   python3 serve.py --host 192.168.1.50 --port 8080
Then set RESHOP_SERVER in source/main.c to http://192.168.1.50:8080 and rebuild.
Icons need tex3ds (ships with devkitPro) to pack apps.t3x; without it the app
falls back to its bundled sprites.
"""
import argparse, json, os, shutil, subprocess, tempfile
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
APPS = os.path.join(HERE, "apps")
ROOT = os.path.join(HERE, "www")
SECTION = os.path.join(ROOT, "reShop", "cdn", "section", "1")
NEWS = os.path.join(ROOT, "reShop", "news")

def build(base):
    os.makedirs(SECTION, exist_ok=True); os.makedirs(NEWS, exist_ok=True)
    entries, icons = [], []
    for f in sorted(os.listdir(APPS)):
        stem, ext = os.path.splitext(f)
        if ext.lower() not in (".cia", ".3dsx"):
            continue
        meta = {}
        mp = os.path.join(APPS, stem + ".json")
        if os.path.exists(mp):
            meta = json.load(open(mp))
        dest = os.path.join(ROOT, "reShop", "files", f)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(APPS, f), dest)
        entries.append({
            "name": meta.get("name", stem),
            "desc": meta.get("desc", "No description."),
            "url": f"{base}/reShop/files/{f}",
            "size": str(os.path.getsize(dest)),   # app reads this as the byte total
            "type": ext.lower().lstrip("."),
        })
        icons.append(os.path.join(APPS, stem + ".png"))
    json.dump({"apps": entries}, open(os.path.join(SECTION, "applisting.json"), "w"), indent=2)

    if not os.path.exists(os.path.join(NEWS, "today.txt")):
        open(os.path.join(NEWS, "today.txt"), "w").write("Welcome to reShop!")

    # pack icons (index i must match listing order) -> apps.t3x
    if shutil.which("tex3ds") and icons:
        from PIL import Image
        with tempfile.TemporaryDirectory() as td:
            names = []
            for i, p in enumerate(icons):
                out = os.path.join(td, f"{i}.png")
                (Image.open(p).convert("RGBA") if os.path.exists(p)
                 else Image.new("RGBA", (64, 64), (180, 190, 200, 255))).resize((64, 64)).save(out)
                names.append(f"{i}.png")
            open(os.path.join(td, "apps.t3s"), "w").write("--atlas -f rgba8888 -z auto\n" + "\n".join(names) + "\n")
            subprocess.run(["tex3ds", "-i", "apps.t3s", "-o", os.path.join(SECTION, "apps.t3x")], cwd=td, check=True)
    else:
        print("note: tex3ds or icons missing; no apps.t3x built (app uses bundled sprites)")
    print(f"listing: {len(entries)} app(s)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", required=True, help="your PC's LAN IP, as the 3DS sees it")
    ap.add_argument("--port", type=int, default=8080)
    a = ap.parse_args()
    os.makedirs(APPS, exist_ok=True)
    build(f"http://{a.host}:{a.port}")
    h = partial(SimpleHTTPRequestHandler, directory=ROOT)
    print(f"serving on 0.0.0.0:{a.port}  (3DS must be on the same network)")
    ThreadingHTTPServer(("0.0.0.0", a.port), h).serve_forever()
