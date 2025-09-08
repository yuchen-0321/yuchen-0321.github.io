#!/bin/bash
echo "同步筆記..."
python3 scripts/sync_obsidian_to_hugo.py

echo "啟動本地伺服器..."
cd hugo-site
hugo server -D
