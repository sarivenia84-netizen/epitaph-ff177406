#!/usr/bin/env python3
import os
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Roses are red, violets are blue, I'm six feet under - and still avoiding you.")
