# AGENTS.md

This file provides comprehensive guidance for AI coding agents working with the Skill Seekers Configs repository.

## Project Overview

**Skill Seekers Configs** is a community repository of JSON configuration files for the [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) tool. These configs tell Skill Seekers how to scrape documentation websites and/or GitHub repositories to generate AI skills compatible with Claude AI.

**Key Characteristics:**
- This repository contains **no source code**, **no build system**, and **no tests**
- Work here is purely authoring, validating, and maintaining JSON configuration files
- Configs are consumed by the external `skill-seekers` Python CLI tool
- The repository serves as a central registry that Skill Seekers can fetch configs from via API

## Repository Structure

```
skill-seekers-configs/
├── official/                    # Verified, production-ready configs
│   ├── web-frameworks/         # React, Vue, Django, FastAPI, Laravel, Astro, Hono
│   ├── game-engines/           # Godot
│   ├── devops/                 # Kubernetes, Ansible
│   ├── css-frameworks/         # Tailwind
│   ├── development-tools/      # Claude Code
│   ├── gaming/                 # Steam Economy
│   └── test-examples/          # Templates and limited-page test configs
├── community/                   # Community-submitted configs pending review
│   └── .gitkeep                # Empty directory marker
└── .github/
    └── ISSUE_TEMPLATE/         # GitHub issue templates for config submissions
```

## Configuration File Formats

### 1. Simple Format (Single-Source Documentation Scraping)

Used for scraping a single documentation website.

```json
{
  "name": "framework-name",
  "description": "When to use this skill...",
  "base_url": "https://docs.example.com/",
  "start_urls": [
    "https://docs.example.com/getting-started",
    "https://docs.example.com/api"
  ],
  "selectors": {
    "main_content": "article, main, div[role='main']",
    "title": "h1, title",
    "code_blocks": "pre code, pre"
  },
  "url_patterns": {
    "include": ["/docs/", "/guide/", "/api/"],
    "exclude": ["/blog/", "/search/", "/_static/"]
  },
  "categories": {
    "getting_started": ["introduction", "getting-started", "quick", "setup"],
    "core_concepts": ["concept", "fundamental", "architecture"],
    "api_reference": ["api", "reference", "method", "function"]
  },
  "rate_limit": 0.5,
  "max_pages": 300
}
```

### 2. Unified Format (Multi-Source: Documentation + GitHub)

Used for combining documentation scraping with GitHub repository analysis (C3.x codebase analysis features).

```json
{
  "name": "framework-name",
  "description": "Complete framework knowledge combining docs and codebase...",
  "merge_mode": "rule-based",
  "sources": [
    {
      "type": "documentation",
      "base_url": "https://docs.example.com/",
      "extract_api": true,
      "selectors": {
        "main_content": "article",
        "title": "h1",
        "code_blocks": "pre code"
      },
      "url_patterns": {
        "include": ["/docs/"],
        "exclude": ["/blog/"]
      },
      "categories": {
        "getting_started": ["intro", "quickstart"],
        "api": ["api", "reference"]
      },
      "rate_limit": 0.5,
      "max_pages": 200
    },
    {
      "type": "github",
      "repo": "owner/repo",
      "enable_codebase_analysis": true,
      "code_analysis_depth": "deep",
      "fetch_issues": true,
      "max_issues": 100,
      "fetch_changelog": true,
      "fetch_releases": true,
      "file_patterns": [
        "src/**/*.py",
        "lib/**/*.py"
      ]
    }
  ]
}
```

### 3. PDF Extraction Format

For extracting content from PDF files.

```json
{
  "name": "example_manual",
  "description": "PDF extraction configuration...",
  "pdf_path": "docs/manual.pdf",
  "extract_options": {
    "chunk_size": 10,
    "min_quality": 5.0,
    "extract_images": true,
    "min_image_size": 100
  },
  "categories": {
    "getting_started": ["introduction", "setup"]
  }
}
```

## Configuration Schema Reference

### Common Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Config identifier (lowercase, hyphen-separated) |
| `description` | string | Yes | Explains WHEN to use the skill, lists capabilities |
| `base_url` | string | Simple only | Base URL of documentation site |
| `start_urls` | array | No | Entry points for crawling (defaults to base_url) |
| `selectors` | object | Yes | CSS selectors for content extraction |
| `url_patterns` | object | No | Include/exclude URL patterns |
| `categories` | object | Yes | Topic organization with keywords |
| `rate_limit` | number | Yes | Delay between requests (seconds) |
| `max_pages` | number | Yes | Maximum pages to scrape |
| `merge_mode` | string | Unified only | How to merge sources: `"rule-based"` or `"claude-enhanced"` |
| `sources` | array | Unified only | Array of documentation and github sources |

### Selector Fields

| Field | Description | Best Practice |
|-------|-------------|---------------|
| `main_content` | Primary content container | Use semantic HTML with fallbacks: `"article, main, div[role='main'], .content"` |
| `title` | Page title | Use `"h1, title"` with fallbacks |
| `code_blocks` | Code examples | Use `"pre code, pre, .highlight"` |

### URL Patterns

| Pattern Type | Purpose | Examples |
|--------------|---------|----------|
| `include` | Paths to crawl | `["/docs/", "/api/", "/guide/"]` |
| `exclude` | Paths to skip | `["/blog/", "/search/", "/_static/"]` |

### GitHub Source Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `"github"` |
| `repo` | string | Repository in `owner/repo` format |
| `enable_codebase_analysis` | boolean | Enable C3.x codebase analysis |
| `code_analysis_depth` | string | `"shallow"` or `"deep"` |
| `fetch_issues` | boolean | Fetch recent issues |
| `max_issues` | number | Maximum issues to fetch |
| `fetch_changelog` | boolean | Fetch CHANGELOG.md |
| `fetch_releases` | boolean | Fetch release notes |
| `file_patterns` | array | Glob patterns for source files to analyze |

## Quality Standards

All production configs in `official/` must meet HIGH quality standards defined in [QUALITY_GUIDELINES.md](QUALITY_GUIDELINES.md):

### Category Requirements
- **5-13 category groups** per config
- **3-6 keywords per category**
- Categories must cover all major documentation sections
- Keywords should match actual URL segments and page headings
- No overlap between category keywords
- No catch-all "other" category

### Selector Requirements
- Use semantic HTML first: `article, main, div[role='main']`
- Provide fallback chains (comma-separated selectors)
- Avoid fragile ID selectors like `#specific-id-123`
- Test selectors against current documentation

### Description Requirements
- Explain **when** to use the skill (not what the framework is)
- List key capabilities covered
- Mention version if applicable
- Keep to 1-3 sentences (concise but informative)

**Good Example:**
```
"Use when working with React, including hooks, components, state management, and modern React patterns. Covers React 18+ features including Concurrent Mode, Suspense, and Server Components."
```

### Rate Limit Guidelines

| Site Type | Rate Limit | Rationale |
|-----------|------------|-----------|
| Large open source docs (React, Vue, Django) | 0.3-0.5s | Well-resourced servers |
| Official vendor docs (Tailwind, FastAPI) | 0.5s | Balanced approach |
| Partner/commercial docs (Steam) | 0.7s | Conservative, respect resources |
| Small project docs | 0.3s | Usually lightweight servers |

## File Naming Conventions

| Config Type | Naming Pattern | Example |
|-------------|----------------|---------|
| Simple (docs only) | `<framework>.json` | `react.json` |
| Unified (docs + GitHub) | `<framework>_unified.json` | `react_unified.json` |
| Test/Template | `<purpose>-test.json` or `template-example.json` | `fastapi_unified_test.json` |

## Config Placement Rules

| Directory | Purpose | Quality Requirement |
|-----------|---------|---------------------|
| `official/<category>/` | Production configs | HIGH quality, fully tested |
| `community/` | Pending review | Any working config |
| `official/test-examples/` | Testing/demonstration | Mark with `⚠️ TEST` in description |

## Validation Commands

Since this repository has no build system, validation is done via the external `skill-seekers` CLI tool:

```bash
# Validate config structure
skill-seekers-validate configs/myconfig.json

# Estimate page count before full scrape
skill-seekers estimate myconfig.json

# Dry-run (no actual scraping, validates selectors and URLs)
skill-seekers scrape --config myconfig.json --dry-run

# Fetch a config by name from this repo via API
skill-seekers fetch-config react
```

## Adding a New Config

1. **Copy the template**: Start from `official/test-examples/template-example.json`

2. **Configure for your target**:
   - Replace `base_url` and `start_urls`
   - Test selectors using browser DevTools
   - Customize categories based on actual docs structure
   - Set appropriate `rate_limit` and `max_pages`

3. **Validate**:
   ```bash
   skill-seekers scrape --config your-config.json --dry-run
   ```

4. **Place in correct directory**:
   - Production configs: `official/<category>/<framework>_unified.json`
   - Experimental configs: `community/<framework>.json`

5. **Update README.md**: Add to the config list and update stats

## Testing Strategy

- **Dry-run testing**: Always test with `--dry-run` before committing
- **Limited page testing**: Use `max_pages: 10-20` for initial testing
- **Selector testing**: Use browser DevTools to verify selectors:
  ```javascript
  document.querySelector('article, main, div[role="main"]')
  ```

## Submission Process

Community contributions are submitted via GitHub Issues using the template at `.github/ISSUE_TEMPLATE/submit-config.md`:

1. Test your config thoroughly
2. Create a submission issue with the template
3. Maintainers review and test
4. Upon approval, config is moved to `official/`

## C3.x Codebase Analysis Features

Skill Seekers v2.6.0+ supports advanced codebase analysis (C3.x features):

- **Design Pattern Detection** (C3.1) - Detect 10 common patterns with 87% precision
- **Test Example Extraction** (C3.2) - Extract real usage from tests
- **How-To Guide Generation** (C3.3) - Auto-generate tutorials
- **Configuration Pattern Extraction** (C3.4) - Analyze config files
- **Architectural Overview** (C3.5) - Generate ARCHITECTURE.md
- **AI Enhancement** (C3.6) - AI-powered insights
- **Architectural Pattern Detection** (C3.7) - Detect MVC, MVVM, Clean Architecture
- **Standalone Codebase Scraper** (C3.8) - Generate 300+ line SKILL.md files

Enable these by setting `enable_codebase_analysis: true` in GitHub source configurations.

## Related Files

- [README.md](README.md) - Project overview and usage instructions
- [QUALITY_GUIDELINES.md](QUALITY_GUIDELINES.md) - Detailed quality standards
- [CLAUDE.md](CLAUDE.md) - Claude Code specific guidance (this file's predecessor)
- `.github/ISSUE_TEMPLATE/submit-config.md` - Config submission template

## External Resources

- **Main Project**: https://github.com/yusufkaraaslan/Skill_Seekers
- **PyPI Package**: `pip install skill-seekers`
- **API**: https://api.skillseekersweb.com

## License

MIT License - Same as Skill Seekers
