#encoding:utf-8
import os, re, codecs, csv

trans = {}
pattern = re.compile(r'new "[^\u4e00-\u9fa5\n]*"')

with open("BKPowers.csv", 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        old = pattern.search(row["old"]).group(0)
        trans[old] = row["new"]

target_file = open("../../Brothel_King-v0.3t-Chinese/tl/schinese/BKPowers.rpy", "r", encoding="utf-8")

with open("BKPowers.rpy", "w", encoding="utf-8") as out_file:
    for line in target_file:
        m = pattern.search(line)
        if m:
            old = m.group(0)
            new = f'new "{trans.get(old, "")}"' 
            print(old, "->", new)
            line = line.replace(old, new)
        out_file.write(line)