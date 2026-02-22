# Skill Seekers Configs

**Community repository for [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) configuration files**

Convert any documentation website into a Claude AI skill using these pre-configured scrapers!

## ✨ v2.6.0+ Support - C3.x Codebase Analysis Features

This repository supports **Skill Seekers v2.6.0+** with the complete C3.x codebase analysis suite:
- 🔍 **Design Pattern Detection** (C3.1) - Detect 10 common patterns with 87% precision
- 🧪 **Test Example Extraction** (C3.2) - Extract real usage from tests
- 📚 **How-To Guide Generation** (C3.3) - Auto-generate tutorials with AI enhancement
- ⚙️ **Configuration Pattern Extraction** (C3.4) - Analyze config files with security insights
- 🏗️ **Architectural Overview** (C3.5) - Generate comprehensive ARCHITECTURE.md
- 🧠 **AI Enhancement** (C3.6) - AI-powered insights for patterns and examples
- 🏛️ **Architectural Pattern Detection** (C3.7) - Detect MVC, MVVM, Clean Architecture
- 📄 **Standalone Codebase Scraper** (C3.8) - Generate 300+ line SKILL.md files

**See unified configs for C3.x feature demonstrations.**

---

## 📦 Available Configs (50+ Official Configs!)

### Web Frameworks (17 configs)
- **nextjs** ⭐ NEW - Next.js React framework with App Router
- **react** - React framework for building UIs
- **vue** - Vue.js progressive framework
- **nuxt** ⭐ NEW - Vue.js framework with SSR/SSG
- **svelte** ⭐ NEW - Svelte compiler and runtime
- **sveltekit** ⭐ NEW - SvelteKit full-stack framework
- **angular** ⭐ NEW - Angular TypeScript framework
- **django** - Django Python web framework
- **flask** ⭐ NEW - Flask Python micro framework
- **ruby-on-rails** ⭐ NEW - Ruby on Rails framework
- **laravel** - Laravel PHP framework
- **fastapi** - FastAPI modern Python framework
- **express** ⭐ NEW - Express.js Node.js framework
- **nestjs** ⭐ NEW - NestJS TypeScript framework
- **astro** - Astro static site generator
- **hono** - Hono lightweight web framework

### Databases (4 configs) 
- **postgresql** ⭐ NEW - PostgreSQL relational database
- **mongodb** ⭐ NEW - MongoDB document database
- **redis** ⭐ NEW - Redis in-memory data store
- **prisma** ⭐ NEW - Prisma ORM

### Data Science (4 configs)
- **pandas** ⭐ NEW - Pandas data analysis library
- **numpy** ⭐ NEW - NumPy numerical computing
- **pytorch** ⭐ NEW - PyTorch deep learning
- **tensorflow** ⭐ NEW - TensorFlow machine learning

### AI/ML (1 config) ⭐ NEW CATEGORY
- **openai-api** ⭐ NEW - OpenAI API (GPT, DALL-E, Whisper)

### DevOps (6 configs)
- **docker** ⭐ NEW - Docker containerization
- **kubernetes** - Kubernetes container orchestration
- **github-actions** ⭐ NEW - GitHub Actions CI/CD
- **terraform** ⭐ NEW - Terraform infrastructure as code
- **ansible** - Ansible automation platform
- **helm** ⭐ NEW - Helm package manager for Kubernetes

### Cloud (1 config) ⭐ NEW CATEGORY
- **aws-boto3** ⭐ NEW - AWS SDK for Python

### Mobile (2 configs) ⭐ NEW CATEGORY
- **react-native** ⭐ NEW - React Native mobile framework
- **flutter** ⭐ NEW - Flutter UI toolkit

### Testing (4 configs) ⭐ NEW CATEGORY
- **jest** ⭐ NEW - JavaScript testing framework
- **cypress** ⭐ NEW - E2E testing framework
- **playwright** ⭐ NEW - Cross-browser testing
- **pytest** ⭐ NEW - Python testing framework

### Search (1 config) ⭐ NEW CATEGORY
- **elasticsearch** ⭐ NEW - Elasticsearch search engine

### Build Tools (1 config) ⭐ NEW CATEGORY
- **vite** ⭐ NEW - Vite build tool

### API Technology (1 config) ⭐ NEW CATEGORY
- **graphql** ⭐ NEW - GraphQL API specification

### Game Engines (1 config)
- **godot** - Godot game engine

### CSS Frameworks (1 config)
- **tailwind** - Tailwind CSS utility framework

### Development Tools (1 config)
- **claude-code** - Claude Code CLI documentation

### Gaming (1 config)
- **steam-economy** - Steam Economy documentation

### Test/Examples (4 configs)
- **httpx_comprehensive** - Complete C3.x codebase analysis example
- **react_unified** - React docs + GitHub with C3.x analysis
- **django_unified** - Django docs + GitHub with C3.x analysis
- **template-example** - Template for new configs

---

## 🚀 Usage

### Option 1: Use MCP Tool (Recommended)
```python
# In Claude Code
fetch_config(config_name='nextjs')
```

### Option 2: Download Manually
```bash
# Download specific config
curl -O https://raw.githubusercontent.com/yusufkaraaslan/skill-seekers-configs/main/official/web-frameworks/nextjs.json

# Use with Skill Seekers
skill-seekers scrape --config nextjs.json
```

### Option 3: Use API
```bash
# Download via Skill Seekers API
curl -O https://api.skillseekersweb.com/api/download/nextjs.json
```

---

## 📝 Submit Your Config

Have a config for a popular framework or tool? Share it with the community!

1. **Test your config** - Make sure it works with Skill Seekers
2. **Validate your config** - Run `python scripts/validate-config.py your-config.json`
3. **Submit via Issue** - [Create submission issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues/new?template=submit-config.md)
4. **Review process** - Maintainers will test and approve
5. **Published!** - Your config becomes available to everyone

---

## ⭐ Quality Standards

All configs in this repository follow strict quality guidelines to ensure reliability and comprehensive coverage.

**See [QUALITY_GUIDELINES.md](QUALITY_GUIDELINES.md) for detailed standards including:**
- Category quality checklist (5-13 categories, 3-6 keywords each)
- Selector fallback chains (semantic HTML, resilient)
- Description best practices (explain when to use, list capabilities)
- Rate limiting guidelines (0.3-0.7s based on server type)
- URL pattern optimization (specific includes, comprehensive excludes)

**Config Quality Levels:**
- **HIGH Quality** (15+ configs): Next.js, Docker, PostgreSQL, Kubernetes, React, etc.
- **Production Ready** (30+ configs): FastAPI, Vue, Tailwind, Astro, etc.
- **Test/Examples** (4 configs): Clearly marked for testing and demonstration

---

## 🔧 Validation

We provide a validation script to check config quality:

```bash
# Validate a single config
python scripts/validate-config.py official/web-frameworks/react.json

# Validate all configs in a directory
python scripts/validate-config.py official/
```

The validator checks:
- Required fields and structure
- Category count and keyword coverage
- Selector quality (fallback chains)
- Description length and content
- Rate limits and max_pages
- Metadata completeness

---

## 📂 Repository Structure

```
skill-seekers-configs/
├── official/                    # Verified, tested configs
│   ├── web-frameworks/         # 17 web frameworks
│   ├── databases/              # 4 databases
│   ├── data-science/           # 4 data science tools
│   ├── ai-ml/                  # 1 AI/ML config ⭐ NEW
│   ├── devops/                 # 6 DevOps tools
│   ├── cloud/                  # 1 cloud SDK ⭐ NEW
│   ├── mobile/                 # 2 mobile frameworks ⭐ NEW
│   ├── testing/                # 4 testing tools ⭐ NEW
│   ├── search/                 # 1 search engine ⭐ NEW
│   ├── build-tools/            # 1 build tool ⭐ NEW
│   ├── api-tech/               # 1 API technology ⭐ NEW
│   ├── game-engines/           # 1 game engine
│   ├── css-frameworks/         # 1 CSS framework
│   ├── development-tools/      # 1 dev tool
│   ├── gaming/                 # 1 gaming platform
│   └── test-examples/          # 4 test configs
├── community/                   # Community-submitted configs (pending review)
├── scripts/                     # Validation and utility scripts
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

- **Total Official Configs**: 50+
- **New in This Release**: 30+ configs
- **Categories**: 16 major categories
- **Quality Level**: All production configs validated to HIGH or Production Ready standards
- **Skill Seekers Compatibility**: v2.6.0+ (with full C3.x codebase analysis support)

---

## 🤝 Contributing

**Quality First!** All submissions must meet our quality standards.

1. **Review [QUALITY_GUIDELINES.md](QUALITY_GUIDELINES.md)** - Learn best practices
2. **Review [CONTRIBUTING.md](CONTRIBUTING.md)** - Detailed contribution guide
3. **Use the template** from `official/test-examples/template-example.json`
4. **Validate your config** with `python scripts/validate-config.py your-config.json`
5. **Test thoroughly** with dry-run mode (`skill-seekers scrape --config your-config.json --dry-run`)
6. **Submit** via pull request or [submission issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues/new)

**Target HIGH quality from the start:**
- 5-13 comprehensive categories
- Selector fallback chains
- Clear, detailed description
- Tested and validated

---

## 📄 License

MIT License - Same as [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

---

**Questions?** Open an [issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues) or ask in [Discussions](https://github.com/yusufkaraaslan/skill-seekers-configs/discussions)
