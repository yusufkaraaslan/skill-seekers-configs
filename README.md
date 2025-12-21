# Skill Seekers Configs

**Community repository for [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) configuration files**

Convert any documentation website into a Claude AI skill using these pre-configured scrapers!

---

## 📦 Available Configs (24 Total)

### Web Frameworks (7 configs)
- **react.json** - React framework for building UIs
- **vue.json** - Vue.js progressive framework
- **django.json** - Django Python web framework
- **laravel.json** - Laravel PHP framework
- **fastapi.json** - FastAPI modern Python framework
- **astro.json** - Astro static site generator
- **hono.json** - Hono web framework

### Game Engines (2 configs)
- **godot.json** - Godot game engine
- **godot-large-example.json** - Godot large documentation example

### DevOps (2 configs)
- **kubernetes.json** - Kubernetes container orchestration
- **ansible-core.json** - Ansible automation platform

### CSS Frameworks (1 config)
- **tailwind.json** - Tailwind CSS utility framework

### Development Tools (1 config)
- **claude-code.json** - Claude Code documentation

### Gaming (1 config)
- **steam-economy-complete.json** - Steam Economy documentation

### Test/Examples (10 configs)
- Unified multi-source configs (docs + GitHub + PDF)
- GitHub-only scraping examples
- PDF extraction examples
- Test configurations

---

## 🚀 Usage

### Option 1: Use MCP Tool (Recommended)
```python
# In Claude Code
fetch_config(config_name='react')
```

### Option 2: Download Manually
```bash
# Download specific config
curl -O https://raw.githubusercontent.com/yusufkaraaslan/skill-seekers-configs/main/official/web-frameworks/react.json

# Use with Skill Seekers
skill-seekers scrape --config react.json
```

### Option 3: Use API
```bash
# Download via Skill Seekers API
curl -O https://api.skillseekersweb.com/api/download/react.json
```

---

## 📝 Submit Your Config

Have a config for a popular framework or tool? Share it with the community!

1. **Test your config** - Make sure it works with Skill Seekers
2. **Submit via Issue** - [Create submission issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues/new?template=submit-config.md)
3. **Review process** - Maintainers will test and approve
4. **Published!** - Your config becomes available to everyone

---

## 📂 Repository Structure

```
skill-seekers-configs/
├── official/                    # Verified, tested configs
│   ├── web-frameworks/         # Web development frameworks
│   ├── game-engines/           # Game development engines
│   ├── devops/                 # DevOps tools
│   ├── css-frameworks/         # CSS frameworks
│   ├── development-tools/      # Developer tools
│   ├── gaming/                 # Gaming platforms
│   └── test-examples/          # Test and example configs
├── community/                   # Community-submitted configs (pending review)
└── .github/
    └── ISSUE_TEMPLATE/         # Submission templates
```

---

## 🔗 Links

- **Main Project**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)
- **PyPI Package**: [pip install skill-seekers](https://pypi.org/project/skill-seekers/)
- **API**: [api.skillseekersweb.com](https://api.skillseekersweb.com)
- **Documentation**: [Skill Seekers README](https://github.com/yusufkaraaslan/Skill_Seekers#readme)

---

## 📊 Stats

- **Total Configs**: 24
- **Categories**: 7
- **Community Contributions**: Coming soon! (A1.3 in progress)

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**Quick Start:**
1. Fork this repository
2. Add your config to `community/`
3. Test with Skill Seekers
4. Submit pull request or create issue

---

## 📄 License

MIT License - Same as [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

---

**Questions?** Open an [issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues) or ask in [Discussions](https://github.com/yusufkaraaslan/skill-seekers-configs/discussions)
