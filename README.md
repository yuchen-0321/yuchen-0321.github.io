# Personal Knowledge Base

**Live Site**: https://yuchen-0321.github.io

A personal knowledge management system that seamlessly integrates Obsidian with Hugo static site generator, automatically publishing your notes to a beautiful website.

## Architecture

```
my-knowledge-base/
├── obsidian-vault/          # Obsidian notes
│   ├── 01-daily-notes/      # Daily notes (not published)
│   ├── 02-permanent-notes/  # Published notes
│   ├── 03-projects/         # Project documentation
│   ├── 04-references/       # Reference materials
│   └── 99-attachments/      # Images, templates, etc.
├── hugo-site/               # Hugo website
├── scripts/                 # Sync scripts
└── publish.sh               # Quick publish script
```

## Quick Start

### Prerequisites

- [Obsidian](https://obsidian.md/)
- [Hugo](https://gohugo.io/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yuchen-0321/yuchen-0321.github.io.git ~/Documents/my-knowledge-base
   cd ~/Documents/my-knowledge-base
   ```

2. **Install Python dependencies**
   ```bash
   pip3 install pyyaml python-frontmatter
   ```

3. **Set up shell aliases** (optional but recommended)
   ```bash
   echo '
   # Knowledge Base shortcuts
   alias kb="cd ~/Documents/my-knowledge-base"
   alias kb-edit="open -a Obsidian ~/Documents/my-knowledge-base/obsidian-vault"
   alias kb-publish="cd ~/Documents/my-knowledge-base && ./publish.sh"
   alias kb-preview="cd ~/Documents/my-knowledge-base && ./preview.sh"
   ' >> ~/.zshrc
   source ~/.zshrc
   ```

## Usage

### Writing Notes

1. Open Obsidian and navigate to the vault:
   ```bash
   kb-edit  # or open Obsidian manually
   ```

2. Create notes in the appropriate folders:
   - `02-permanent-notes/` for published content
   - `01-daily-notes/` for personal notes (not published)

3. Use frontmatter for metadata:
   ```yaml
   ---
   title: "Your Note Title"
   date: 2025-01-20
   tags: ["tag1", "tag2"]
   categories: ["category"]
   ---
   ```

### Publishing

**Quick publish** (recommended):
```bash
./publish.sh
```

**Manual steps**:
```bash
# 1. Sync notes
python3 scripts/sync_obsidian_to_hugo.py

# 2. Commit and push
git add .
git commit -m "Update content"
git push
```

### Local Preview

```bash
./preview.sh
# Visit http://localhost:1313
```

## Configuration

### Website Settings

Edit `hugo-site/config.yml`:

```yaml
title: "Your Knowledge Base"
author: "Your Name"
description: "Your personal knowledge base"
baseURL: "https://yourusername.github.io"
```

### Obsidian Settings

1. Install recommended plugins:
   - Templater
   - Tag Wrangler
   - Calendar

2. Set up templates in `99-attachments/templates/`

## Troubleshooting

### Common Issues

**Sync script errors**:
```bash
# Check Python packages
pip3 list | grep -E "yaml|frontmatter"

# Reinstall if needed
pip3 install --upgrade pyyaml python-frontmatter
```

**Website not updating**:
```bash
# Check GitHub Actions status
open https://github.com/yourusername/yourusername.github.io/actions

# Force rebuild
git commit --allow-empty -m "Trigger rebuild"
git push
```

**Hugo preview fails**:
```bash
# Update Hugo
brew upgrade hugo  # macOS
```

## File Organization

### Note Categories

- **Daily Notes** (`01-daily-notes/`): Personal, not published
- **Permanent Notes** (`02-permanent-notes/`): Main content, published
- **Projects** (`03-projects/`): Project documentation
- **References** (`04-references/`): Reference materials
- **Attachments** (`99-attachments/`): Images, templates

### Recommended Workflow

1. **Daily**: Write in Obsidian, publish with `kb-publish`
2. **Weekly**: Organize tags and categories
3. **Monthly**: Update Hugo theme and settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Obsidian](https://obsidian.md/) for the amazing note-taking experience
- [Hugo](https://gohugo.io/) for the fast static site generator
- [GitHub Pages](https://pages.github.com/) for free hosting

## Support

- Check the [Issues](https://github.com/yuchen-0321/yuchen-0321.github.io/issues) page
- Review the [操作指南](操作指南.md) for detailed instructions

---

**🌟 Star this repository if you find it useful!**
