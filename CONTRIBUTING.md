# Contributing to Skill Seekers Configs

Thank you for your interest in contributing! This guide will help you create high-quality configuration files for the Skill Seekers project.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Creating a Config](#creating-a-config)
3. [Quality Standards](#quality-standards)
4. [Testing Your Config](#testing-your-config)
5. [Submission Process](#submission-process)
6. [Common Issues](#common-issues)

---

## Getting Started

### What is a Config?

A config file tells Skill Seekers how to scrape documentation and/or GitHub repositories to create AI skills. Configs are JSON files that specify:
- Where to find documentation
- What content to extract
- How to organize the content
- Which codebases to analyze

### Prerequisites

- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) installed
- Python 3.10+ (for validation script)
- Familiarity with CSS selectors
- Access to the documentation site you want to scrape

---

## Creating a Config

### Step 1: Choose Your Format

#### Simple Format (Documentation Only)
Use when you only need to scrape documentation.

#### Unified Format (Documentation + GitHub) ⭐ Recommended
Use when you want both documentation and source code analysis. Provides the most comprehensive skill.

### Step 2: Copy the Template

```bash
cp official/test-examples/template-example.json my-config.json
```

### Step 3: Fill in Basic Information

```json
{
  "name": "your-framework",
  "description": "Use when working with [Framework] for [use case]. Covers [feature 1], [feature 2], and [feature 3].",
  "base_url": "https://docs.example.com/",
  ...
}
```

**Name guidelines:**
- Lowercase with hyphens
- No special characters
- Be specific but concise
- Examples: `nextjs`, `docker`, `postgresql`

**Description guidelines:**
- Start with "Use when..." or "Use for..."
- Explain when to use the skill
- List 3-5 key capabilities
- Include version if relevant
- 50-150 characters

### Step 4: Configure Selectors

Test selectors using browser DevTools:

```javascript
// In browser console on the documentation site
document.querySelector('article, main, div[role="main"]')
```

**Best practices:**
- Use semantic HTML first: `article`, `main`
- Provide fallback chains: `article, main, div[role='main']`
- Avoid ID selectors: `#specific-id` (fragile)
- Test on multiple pages

### Step 5: Define Categories

Categories organize content for the AI. Each category needs:
- Clear name (e.g., `routing`, `authentication`)
- 3-6 relevant keywords
- Keywords should match URL paths and headings

**Example:**
```json
{
  "categories": {
    "routing": ["route", "router", "path", "endpoint", "url", "navigation"],
    "authentication": ["auth", "login", "password", "jwt", "session", "oauth"]
  }
}
```

**Category selection strategy:**
1. Browse the documentation site
2. Identify major sections (getting started, API, guides)
3. Look at URL patterns (`/docs/routing/`, `/docs/auth/`)
4. Extract keywords from page headings
5. Group related concepts

### Step 6: Set Rate Limit

```json
{
  "rate_limit": 0.5
}
```

**Rate limit guidelines:**
- Large open source docs: 0.3-0.5s
- Official vendor docs: 0.5s
- Partner/commercial docs: 0.7s
- Small projects: 0.3s

> **Note:** Do not include `max_pages` in production configs. The default limit is applied automatically. If you need to limit pages for local testing, create a separate test config.

### Step 7: Add GitHub Source (Unified Format)

For the best quality skill, add GitHub source code analysis:

```json
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
    "src/**/*.js",
    "lib/**/*.js"
  ]
}
```

---

## Quality Standards

All configs must meet these standards:

### Category Requirements ✅

- **5-13 categories** per config
- **3-6 keywords** per category
- Categories cover all major documentation sections
- Keywords match actual URL segments and headings
- No overlap between category keywords
- No generic names like "basic", "other", "misc"

### Selector Requirements ✅

- Use semantic HTML first: `article, main`
- Provide fallback chains (comma-separated)
- Avoid fragile ID selectors
- Test selectors against current documentation
- Must include `main_content` selector

### Description Requirements ✅

- Explain **when** to use the skill
- List key capabilities covered
- Mention version if applicable
- 50+ characters
- Start with "Use when..." or "Use for..."

### Metadata (Optional but Recommended) ✅

Add a metadata block for better discoverability:

```json
{
  "metadata": {
    "author": "Framework Author",
    "language": "JavaScript",
    "framework_type": "Web Framework",
    "use_cases": [
      "Use case 1",
      "Use case 2"
    ],
    "related_skills": [
      "related-skill-1",
      "related-skill-2"
    ]
  }
}
```

---

## Testing Your Config

### Step 1: Validate Structure

```bash
python scripts/validate-config.py my-config.json
```

This checks:
- Required fields
- Category quality
- Selector format
- Description length
- Rate limits

**Aim for HIGH quality rating (90+ score).**

### Step 2: Dry-Run Test

```bash
skill-seekers scrape --config my-config.json --dry-run
```

This validates:
- Selectors work on actual pages
- URLs are accessible
- No obvious errors

### Step 3: Limited Page Test

For initial testing, create a separate test config (in `official/test-examples/`) that scrapes only a few start_urls with no include patterns, to limit scope.

Run actual scrape:

```bash
skill-seekers scrape --config my-config-test.json
```

Verify:
- Content is extracted correctly
- Categories are populated
- No broken selectors

### Step 4: Full Test (Optional)

If limited test passes, run full scrape:

```bash
skill-seekers scrape --config my-config.json
```

Review the generated SKILL.md to ensure quality.

---

## Submission Process

### Option 1: Submit via GitHub Issue (Recommended)

1. Go to [New Issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues/new/choose)
2. Select "Submit New Config"
3. Fill out the template
4. Paste your complete config JSON
5. Submit and wait for review

### Option 2: Submit via Pull Request

1. Fork the repository
2. Create a new branch: `git checkout -b add-framework-name`
3. Add your config to appropriate directory
4. Update README.md with new config
5. Commit with clear message: `Add Next.js config`
6. Push and create PR

### Review Process

Maintainers will:
1. Validate your config with the script
2. Test with dry-run mode
3. Check quality standards
4. Provide feedback if needed
5. Merge and publish

**Timeline:** Usually 1-3 days for review.

---

## Common Issues

### Selectors Not Working

**Problem:** Content not being extracted

**Solutions:**
- Test in browser DevTools first
- Use fallback chains: `article, main, div[role='main']`
- Check if site uses dynamic loading (may need different approach)
- Look for class names that might change

### Too Many/Few Pages

**Problem:** Wrong number of pages detected

**Solutions:**
- Refine `url_patterns.include` to be more specific
- Add more entries to `url_patterns.exclude`
- Check that `base_url` has a trailing slash

### Categories Not Matching

**Problem:** Content not organized correctly

**Solutions:**
- Review keywords match actual URLs
- Check case sensitivity
- Add more specific keywords
- Remove overlapping keywords

### Rate Limiting

**Problem:** Getting 429 errors

**Solutions:**
- Increase `rate_limit` (e.g., 0.3 → 0.5)
- Check if site has specific rate limits
- Use more conservative settings

### GitHub Source Issues

**Problem:** Codebase analysis not working

**Solutions:**
- Verify repo name format: `owner/repo`
- Check file_patterns match actual structure
- Ensure repo is public
- Verify `enable_codebase_analysis: true`

---

## Example: Complete Config

See `official/web-frameworks/nextjs.json` for a complete example:

```json
{
  "name": "nextjs",
  "description": "Complete Next.js knowledge...",
  "version": "1.1.0",
  "merge_mode": "rule-based",
  "sources": [
    {
      "type": "documentation",
      "base_url": "https://nextjs.org/docs/",
      "extract_api": true,
      "start_urls": [...],
      "selectors": {
        "main_content": "article, main",
        "title": "h1",
        "code_blocks": "pre code"
      },
      "url_patterns": {
        "include": [...],
        "exclude": [...]
      },
      "categories": {...},
      "rate_limit": 0.5
    },
    {
      "type": "github",
      "repo": "vercel/next.js",
      "enable_codebase_analysis": true,
      "code_analysis_depth": "deep",
      "fetch_issues": true,
      "max_issues": 100,
      "fetch_changelog": true,
      "fetch_releases": true,
      "file_patterns": [...]
    }
  ],
  "metadata": {...}
}
```

---

## Tips for Success

### Before Submitting

- ✅ Test thoroughly with dry-run
- ✅ Validate with the script (aim for 90+ score)
- ✅ Test on multiple documentation pages
- ✅ Check rate limits work
- ✅ Review quality guidelines
- ✅ Use the submission template

### Common Mistakes to Avoid

- ❌ Fragile ID selectors
- ❌ Too few categories (< 5)
- ❌ Too many keywords per category (> 6)
- ❌ Missing fallback selectors
- ❌ Generic category names
- ❌ Not testing before submitting

### Best Practices

- ✅ Use unified format when possible
- ✅ Include GitHub source for open source projects
- ✅ Add metadata block
- ✅ Follow naming conventions
- ✅ Test on actual documentation site
- ✅ Be specific in description

---

## Questions?

- **Config help:** Open a [discussion](https://github.com/yusufkaraaslan/skill-seekers-configs/discussions)
- **Bug reports:** Create an [issue](https://github.com/yusufkaraaslan/skill-seekers-configs/issues)
- **Feature requests:** Use config request template

---

## Recognition

Contributors will be:
- Listed in release notes
- Credited in config metadata
- Thanked in README

Thank you for helping make Skill Seekers better! 🎉
