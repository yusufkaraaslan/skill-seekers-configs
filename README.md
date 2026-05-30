# Skill Seekers Configs

**Community repository for [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) configuration files**

Convert any documentation website into an AI skill using these pre-configured scrapers!

> **Skill Seekers v3.6.0+** — 178 production configs across 21 categories.

---

## 📦 Official Configs (178 across 21 categories)

### Game Engines (35 configs)
Unity, Unreal Engine, Godot, Bevy, Phaser, Babylon.js, PlayCanvas, GameMaker, GDevelop, Defold, Solar2D, Cocos2d, Pygame, Raylib, LÖVE, Ren'Py, Twine, RPG Maker, Construct, Stencyl, MonoGame, HaxeFlixel, Heaps, O3DE, Stride, Flax, Panda3D, Urho3D, Torque3D, Armory3D, PICO-8, AGS, Bitsy, PyGame Zero, Clickteam Fusion

### AI / ML (34 configs)
anthropic, openai-api, huggingface, langchain, llamaindex, pytorch, tensorflow, keras, jax, pytorch-lightning, fastai, deepspeed, onnx, scikit-learn, xgboost, lightgbm, catboost, gensim, spacy, nltk, opencv, pinecone, weaviate, chroma, mlflow, wandb, kubeflow, dvc, ray, matplotlib, seaborn, plotly, modin, cohere

### Web Frameworks (21 configs)
angular, astro, django, express, fastapi, flask, hono, htmx, httpx, laravel, nestjs, nextjs, nuxt, react, react-query, ruby-on-rails, solidjs, svelte, sveltekit, vue, zod

### Databases (16 configs)
postgresql, mongodb, redis, prisma, mysql, sqlite, elasticsearch-db, cassandra, dynamodb, neo4j, couchdb, influxdb, supabase, planetscale, fauna, cockroachdb

### Testing (11 configs)
artillery, cypress, insomnia, jest, k6, playwright, postman, pytest, selenium, testing-library, vitest

### DevOps (9 configs)
docker, kubernetes, github-actions, terraform, ansible, helm, gitlab-ci, jenkins, argocd

### Cloud (9 configs)
aws-boto3, azure-sdk, gcp, aws-cdk, pulumi, serverless, cloudflare-workers, vercel, netlify

### Development Tools (8 configs)
claude-code, vscode, git, neovim, tmux, zsh, homebrew, wsl

### Build Tools (7 configs)
vite, webpack, esbuild, rollup, turbopack, parcel, gradle

### CSS Frameworks (6 configs)
tailwind, bootstrap, chakra-ui, material-ui, shadcn-ui, daisyui

### Data Science (4 configs)
pandas, numpy, pytorch (see AI/ML), tensorflow (see AI/ML)

### Security (3 configs)
auth0, clerk, sentry

### CMS (3 configs)
contentful, strapi, sanity

### Mobile (2 configs)
flutter, react-native

### Messaging (2 configs)
kafka, rabbitmq

### Graphics (2 configs)
opengl, webgpu

### API Technology (2 configs)
graphql, rest-api

### Search (1 config)
elasticsearch

### Payments (1 config)
stripe

### Languages (1 config)
typescript

### Gaming (1 config)
steam-economy

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
curl -O https://raw.githubusercontent.com/yusufkaraaslan/skill-seekers-configs/main/official/web-frameworks/nextjs_unified.json

# Use with Skill Seekers
skill-seekers create --config nextjs_unified.json
```

### Option 3: Use API
```bash
# Download via Skill Seekers API
curl -O https://api.skillseekersweb.com/api/download/nextjs.json
```

---

## 📝 Submit Your Config

Have a config for a popular framework or tool? Share it with the community!

1. **Test your config** — `skill-seekers create --config your-config.json --dry-run`
2. **Validate your config** — `python scripts/validate-config.py your-config.json`
3. **Submit via Issue** — [Create submission issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues/new/choose)
4. **Review process** — Maintainers will test and approve
5. **Published!** — Your config becomes available to everyone

---

## ⭐ Quality Standards

All configs follow strict quality guidelines for reliability and comprehensive coverage.

**See [QUALITY_GUIDELINES.md](QUALITY_GUIDELINES.md) for detailed standards including:**
- Category quality (5-13 categories, 3-6 keywords each)
- Selector fallback chains (semantic HTML, resilient)
- Description best practices (explain when to use, list capabilities)
- Rate limiting guidelines (0.3–0.7s based on server type)
- URL pattern optimization (specific includes, comprehensive excludes)

---

## 🔧 Validation

```bash
# Validate a single config
python scripts/validate-config.py official/web-frameworks/react_unified.json

# Validate all configs in a directory
python scripts/validate-config.py official/
```

---

## 📂 Repository Structure

```
skill-seekers-configs/
├── official/                    # Verified, tested configs (178 configs)
│   ├── ai-ml/                  # 34 AI/ML tools
│   ├── api-tech/               # 2 API technologies
│   ├── build-tools/            # 7 build tools
│   ├── cloud/                  # 9 cloud platforms
│   ├── cms/                    # 3 CMS platforms
│   ├── css-frameworks/         # 6 CSS frameworks
│   ├── data-science/           # 4 data science tools
│   ├── databases/              # 16 databases & ORMs
│   ├── development-tools/      # 8 dev tools
│   ├── devops/                 # 9 DevOps tools
│   ├── game-engines/           # 35 game engines
│   ├── gaming/                 # 1 gaming platform
│   ├── graphics/               # 2 graphics APIs
│   ├── languages/              # 1 language
│   ├── messaging/              # 2 messaging systems
│   ├── mobile/                 # 2 mobile frameworks
│   ├── payments/               # 1 payment platform
│   ├── search/                 # 1 search engine
│   ├── security/               # 3 auth/security tools
│   ├── testing/                # 11 testing tools
│   ├── web-frameworks/         # 21 web frameworks
│   └── test-examples/          # 4 templates & test configs
├── community/                   # Community-submitted configs (pending review)
├── scripts/                     # Validation scripts
└── .github/
    └── ISSUE_TEMPLATE/         # Issue templates for submissions and bug reports
```

---

## 🔗 Links

- **Main Project**: [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)
- **PyPI Package**: [pip install skill-seekers](https://pypi.org/project/skill-seekers/)
- **API**: [api.skillseekersweb.com](https://api.skillseekersweb.com)
- **Website**: [skillseekersweb.com](https://skillseekersweb.com/)

---

## 📊 Stats

- **Total Official Configs**: 178
- **Categories**: 21 production + 1 test-examples
- **Skill Seekers Compatibility**: v3.6.0+
- **Quality Level**: All production configs validated to v1.1.0 standards

---

## 🤝 Contributing

**Quality First!** All submissions must meet our quality standards.

1. **Review [QUALITY_GUIDELINES.md](QUALITY_GUIDELINES.md)** — Learn best practices
2. **Review [CONTRIBUTING.md](CONTRIBUTING.md)** — Detailed contribution guide
3. **Use the template** from `official/test-examples/template-example.json`
4. **Validate** with `python scripts/validate-config.py your-config.json`
5. **Test** with dry-run mode (`skill-seekers create --config your-config.json --dry-run`)
6. **Submit** via [submission issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues/new/choose)

---

## 📄 License

MIT License — Same as [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers)

---

**Questions?** Open an [issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues) or start a [Discussion](https://github.com/yusufkaraaslan/skill-seekers-configs/discussions)
