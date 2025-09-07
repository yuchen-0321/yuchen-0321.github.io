
#!/usr/bin/env python3
"""
Obsidian to Hugo 同步腳本
將 Obsidian Vault 中的筆記同步到 Hugo 網站
"""

import os
import re
import shutil
from pathlib import Path
import frontmatter
from datetime import datetime

class ObsidianHugoSync:
    def __init__(self):
        # 設定路徑
        self.base_dir = Path.cwd()
        self.vault_dir = self.base_dir / "obsidian-vault"
        self.hugo_content_dir = self.base_dir / "hugo-site" / "content" / "posts"
        self.hugo_static_dir = self.base_dir / "hugo-site" / "static"
        
        # 確保目標資料夾存在
        self.hugo_content_dir.mkdir(parents=True, exist_ok=True)
        self.hugo_static_dir.mkdir(parents=True, exist_ok=True)
        
    def convert_wikilinks(self, content):
        """轉換 Obsidian 的 [[]] 連結為 Hugo 格式"""
        pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
        
        def replace_link(match):
            link_target = match.group(1)
            link_text = match.group(2) if match.group(2) else link_target
            link_url = link_target.lower().replace(' ', '-')
            return f'[{link_text}](/posts/{link_url}/)'
        
        return re.sub(pattern, replace_link, content)
    
    def process_frontmatter(self, post, file_path):
        """處理和補充 frontmatter"""
        if 'date' not in post:
            post['date'] = datetime.now().isoformat()
        
        if 'title' not in post:
            post['title'] = file_path.stem.replace('-', ' ').title()
        
        if 'draft' not in post:
            post['draft'] = False
            
        if 'tags' in post and not isinstance(post['tags'], list):
            post['tags'] = [post['tags']]
        
        if 'categories' in post and not isinstance(post['categories'], list):
            post['categories'] = [post['categories']]
            
        return post
    
    def should_sync_file(self, file_path):
        """判斷檔案是否應該同步"""
        skip_dirs = ['99-附件', 'templates', '.obsidian', '.trash']
        
        # 跳過每日筆記（可選）
        if '01-每日筆記' in str(file_path):
            return False
        
        for skip_dir in skip_dirs:
            if skip_dir in str(file_path):
                return False
        
        return True
    
    def sync_file(self, source_file):
        """同步單個檔案"""
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            post = self.process_frontmatter(post, source_file)
            post.content = self.convert_wikilinks(post.content)
            
            filename = source_file.stem.lower().replace(' ', '-') + '.md'
            dest_file = self.hugo_content_dir / filename
            
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            
            print(f"✅ 同步成功: {source_file.name} -> {filename}")
            return True
            
        except Exception as e:
            print(f"❌ 同步失敗: {source_file.name}: {str(e)}")
            return False
    
    def sync_all(self):
        """同步所有檔案"""
        print("🔄 開始同步 Obsidian 筆記到 Hugo...")
        print(f"📁 來源: {self.vault_dir}")
        print(f"📁 目標: {self.hugo_content_dir}\n")
        
        md_files = list(self.vault_dir.glob("**/*.md"))
        sync_files = [f for f in md_files if self.should_sync_file(f)]
        
        print(f"找到 {len(md_files)} 個檔案，準備同步 {len(sync_files)} 個\n")
        
        success_count = 0
        for file_path in sync_files:
            if self.sync_file(file_path):
                success_count += 1
        
        print(f"\n✨ 同步完成！成功 {success_count}/{len(sync_files)} 個檔案")

if __name__ == "__main__":
    syncer = ObsidianHugoSync()
    syncer.sync_all()
