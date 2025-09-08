#!/bin/bash
echo "🔄 同步筆記..."
python3 scripts/sync_obsidian_to_hugo.py

echo "📦 提交變更..."
git add .
git commit -m "Update: $(date '+%Y-%m-%d %H:%M')"

echo "⬆️ 推送到 GitHub..."
git push

echo "✅ 完成！網站將在 2-3 分鐘後更新"
echo "🌐 查看進度: https://github.com/yuchen-0321/yuchen-0321.github.io/actions"
