# 個人知識庫系統

**線上網站**: https://yuchen-0321.github.io  
**English Version**: [README.md](README.md)

一個無縫整合 Obsidian 與 Hugo 靜態網站生成器的個人知識管理系統，自動將您的筆記發布為精美的網站。

## 專案架構

```
my-knowledge-base/
├── obsidian-vault/          # Obsidian 筆記庫
│   ├── 01-每日筆記/         # 每日筆記（不發布）
│   ├── 02-永久筆記/         # 發布的筆記
│   ├── 03-專案/             # 專案文件
│   ├── 04-參考資料/         # 參考材料
│   └── 99-附件/             # 圖片、模板等
├── hugo-site/               # Hugo 網站
├── scripts/                 # 同步腳本
└── publish.sh               # 快速發布腳本
```

## 快速開始

### 環境需求

- [Obsidian](https://obsidian.md/)
- [Hugo](https://gohugo.io/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)

### 安裝步驟

1. **複製儲存庫**
   ```bash
   git clone https://github.com/yuchen-0321/yuchen-0321.github.io.git ~/Documents/my-knowledge-base
   cd ~/Documents/my-knowledge-base
   ```

2. **安裝 Python 依賴套件**
   ```bash
   pip3 install pyyaml python-frontmatter
   ```

3. **設定 Shell 別名**（選用但推薦）
   ```bash
   echo '
   # 知識庫快捷命令
   alias kb="cd ~/Documents/my-knowledge-base"
   alias kb-edit="open -a Obsidian ~/Documents/my-knowledge-base/obsidian-vault"
   alias kb-publish="cd ~/Documents/my-knowledge-base && ./publish.sh"
   alias kb-preview="cd ~/Documents/my-knowledge-base && ./preview.sh"
   ' >> ~/.zshrc
   source ~/.zshrc
   ```

## 使用方式

### 撰寫筆記

1. 開啟 Obsidian 並導航到筆記庫：
   ```bash
   kb-edit  # 或手動開啟 Obsidian
   ```

2. 在適當的資料夾中建立筆記：
   - `02-永久筆記/` 用於發布的內容
   - `01-每日筆記/` 用於個人筆記（不會發布）

3. 使用前置元資料設定筆記屬性：
   ```yaml
   ---
   title: "筆記標題"
   date: 2025-01-20
   tags: ["標籤1", "標籤2"]
   categories: ["分類"]
   ---
   ```

### 發布網站

**快速發布**（推薦）:
```bash
./publish.sh
```

**手動步驟**:
```bash
# 1. 同步筆記
python3 scripts/sync_obsidian_to_hugo.py

# 2. 提交並推送
git add .
git commit -m "更新內容"
git push
```

### 本地預覽

```bash
./preview.sh
# 訪問 http://localhost:1313
```

## 設定配置

### 網站設定

編輯 `hugo-site/config.yml`：

```yaml
title: "您的知識庫"
author: "您的姓名"
description: "您的個人知識庫"
baseURL: "https://yourusername.github.io"
```

### Obsidian 設定

1. 安裝推薦外掛：
   - Templater
   - Tag Wrangler
   - Calendar

2. 在 `99-附件/templates/` 中設定模板

## 故障排除

### 常見問題

**同步腳本錯誤**:
```bash
# 檢查 Python 套件
pip3 list | grep -E "yaml|frontmatter"

# 重新安裝（如需要）
pip3 install --upgrade pyyaml python-frontmatter
```

**網站沒有更新**:
```bash
# 檢查 GitHub Actions 狀態
open https://github.com/yourusername/yourusername.github.io/actions

# 強制重建
git commit --allow-empty -m "觸發重建"
git push
```

**Hugo 預覽失敗**:
```bash
# 更新 Hugo
brew upgrade hugo  # macOS
```

## 檔案組織

### 筆記分類

- **每日筆記** (`01-每日筆記/`): 個人使用，不會發布
- **永久筆記** (`02-永久筆記/`): 主要內容，會發布
- **專案** (`03-專案/`): 專案文件
- **參考資料** (`04-參考資料/`): 參考材料
- **附件** (`99-附件/`): 圖片、模板

### 建議工作流程

1. **每日**: 在 Obsidian 中撰寫，使用 `kb-publish` 發布
2. **每週**: 整理標籤和分類
3. **每月**: 更新 Hugo 主題和設定

## 最佳實踐

### 筆記撰寫

- 使用清晰的標題和結構
- 善用標籤和分類進行組織
- 在筆記間建立連結
- 定期整理和更新內容

### 版本控制

- 經常提交變更
- 撰寫有意義的提交訊息
- 定期備份重要資料
- 使用分支進行實驗性變更

## 進階功能

### 自訂樣式

1. 修改 `hugo-site/assets/css/` 中的 CSS 檔案
2. 在 `hugo-site/layouts/` 中自訂版面
3. 使用 Hugo 短代碼增強功能

### 整合工具

- **圖片處理**: 自動最佳化和壓縮
- **SEO 最佳化**: 自動生成 meta 標籤
- **分析追蹤**: Google Analytics 整合
- **評論系統**: Disqus 或 Utterances

## 貢獻

1. Fork 此儲存庫
2. 建立功能分支
3. 進行變更
4. 提交 Pull Request

## 授權條款

此專案使用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案。

## 致謝

- [Obsidian](https://obsidian.md/) 提供優秀的筆記體驗
- [Hugo](https://gohugo.io/) 提供快速的靜態網站生成
- [GitHub Pages](https://pages.github.com/) 提供免費託管服務

## 支援

- 查看 [Issues](https://github.com/yuchen-0321/yuchen-0321.github.io/issues) 頁面
- 參考 [操作指南](操作指南.md) 取得詳細說明

## 相關資源

- [Hugo 文件](https://gohugo.io/documentation/)
- [Obsidian 說明](https://help.obsidian.md/)
- [GitHub Pages 指南](https://docs.github.com/en/pages)
- [Markdown 語法](https://www.markdownguide.org/)

---

**🌟 如果覺得這個專案有用，請給個星星支持！**
