#!/usr/bin/env python3
import os
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Error 404: Afterlife not found (yet)")