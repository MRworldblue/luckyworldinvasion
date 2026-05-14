import os
import re

client_html_path = r"e:\WORKS\luckyworldinvasion\client_main\modlist.html"
server_mods_dir = r"e:\WORKS\luckyworldinvasion\official_server_repo\mods"

client_mods = set()
with open(client_html_path, "r", encoding="utf-8") as f:
    content = f.read()
    matches = re.findall(r'<a href="[^"]+">(.+?) \(by', content)
    for m in matches:
        normalized = re.sub(r'[^a-z0-9]', '', m.lower())
        client_mods.add(normalized)
        
server_mods = set()
for filename in os.listdir(server_mods_dir):
    if filename.endswith(".jar"):
        base_name = re.split(r'[-+]', filename)[0]
        normalized = re.sub(r'[^a-z0-9]', '', base_name.lower())
        server_mods.add(normalized)

client_only = client_mods - server_mods
server_only = server_mods - client_mods

client_orig = {}
with open(client_html_path, "r", encoding="utf-8") as f:
    for m in re.findall(r'<a href="[^"]+">(.+?) \(by', f.read()):
        norm = re.sub(r'[^a-z0-9]', '', m.lower())
        client_orig[norm] = m

server_orig = {}
for filename in os.listdir(server_mods_dir):
    if filename.endswith(".jar"):
        base_name = re.split(r'[-+]', filename)[0]
        norm = re.sub(r'[^a-z0-9]', '', base_name.lower())
        server_orig[norm] = filename

with open(r"e:\WORKS\luckyworldinvasion\compare_result.md", "w", encoding="utf-8") as out:
    out.write("# 📊 Mod Comparison: Client vs Server\n\n")
    
    out.write("### 🖥️ Client-Only Mods (Likely UI/Optimization/Minimaps)\n")
    out.write("These mods are in `modlist.html` but not found in the server's `mods` folder.\n\n")
    for m in sorted(client_only):
        out.write(f"- {client_orig.get(m, m)}\n")
        
    out.write("\n### 🌐 Server-Only Mods (Likely server utilities or mismatched filenames)\n")
    out.write("These `.jar` files are in the server's `mods` folder but not listed in the client `modlist.html`.\n\n")
    for m in sorted(server_only):
        out.write(f"- {server_orig.get(m, m)}\n")
