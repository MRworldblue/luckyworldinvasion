import os
import re
from collections import Counter

crash_dir = r"e:\WORKS\luckyworldinvasion\crash_reports"
output_file = r"e:\WORKS\luckyworldinvasion\crash_analysis.md"

if not os.path.exists(crash_dir):
    print("Error: crash_reports directory not found.")
    exit(1)

files = [f for f in os.listdir(crash_dir) if f.endswith(".txt")]

total_files = len(files)
kubejs_issues = 0
disk_write_issues = 0
oom_issues = 0
suspected_mods = Counter()
exceptions = Counter()

mod_regex = re.compile(r"Suspected Mods: ([^\n]+)")
exception_regex = re.compile(r"(java\.lang\.[A-Za-z]+Error|java\.lang\.[A-Za-z]+Exception|[A-Za-z]+Exception)")

for filename in files:
    filepath = os.path.join(crash_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
            # Check for KubeJS infinite loop / issues
            if "KubeJS" in content and ("StackOverflowError" in content or "infinite loop" in content.lower()):
                kubejs_issues += 1
            
            # Check for 11TB / Disk write bug
            if "No space left on device" in content or "11TB" in content or "11 TB" in content or "disk full" in content.lower():
                disk_write_issues += 1
                
            # Check for OutOfMemory
            if "OutOfMemoryError" in content:
                oom_issues += 1
                
            # Extract suspected mods if present (often added by some crash reporting mods)
            mods_found = mod_regex.findall(content)
            for mod_list in mods_found:
                for mod in mod_list.split(","):
                    suspected_mods[mod.strip()] += 1
            
            # Extract common exceptions
            excs = exception_regex.findall(content)
            if excs:
                # Count the first prominent exception in the log
                exceptions[excs[0]] += 1
                
    except Exception as e:
        print(f"Error reading {filename}: {e}")

with open(output_file, "w", encoding="utf-8") as out:
    out.write("# 💥 Rapport d'Analyse des Crash Logs (Crash Analyzer)\n\n")
    out.write(f"**Total des rapports analysés :** {total_files}\n\n")
    
    out.write("## ⚠️ Problèmes Majeurs Identifiés\n")
    out.write(f"- **Bug d'écriture disque 11TB / Espace saturé :** {disk_write_issues} occurrences\n")
    out.write(f"- **Boucle Infinie KubeJS (StackOverflow) :** {kubejs_issues} occurrences\n")
    out.write(f"- **Fuite de mémoire (OutOfMemoryError) :** {oom_issues} occurrences\n\n")
    
    out.write("## 🐛 Mods Suspectés Fréquemment\n")
    if suspected_mods:
        for mod, count in suspected_mods.most_common(10):
            out.write(f"- **{mod}** : {count} crash(s)\n")
    else:
        out.write("- *Aucun mod suspecté explicitement identifié par les balises 'Suspected Mods'.*\n")
        
    out.write("\n## 🛑 Exceptions Communes\n")
    if exceptions:
        for exc, count in exceptions.most_common(10):
            out.write(f"- `{exc}` : {count} occurrences\n")
    else:
        out.write("- *Aucune exception standard détectée.*\n")
    
print("Analyse terminée. Résultat généré dans crash_analysis.md.")
