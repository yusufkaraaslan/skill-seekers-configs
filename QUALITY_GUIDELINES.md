# Config Quality Guidelines

This document provides comprehensive guidelines for creating and maintaining high-quality configuration files for the Skill Seekers project.

## Table of Contents

1. [Category Quality](#category-quality)
2. [Selector Quality](#selector-quality)
3. [Description Quality](#description-quality)
4. [Rate Limit Guidelines](#rate-limit-guidelines)
5. [URL Pattern Guidelines](#url-pattern-guidelines)
6. [Quality Metrics](#quality-metrics)

---

## Category Quality

### Excellent Categories Have:

✅ **5-13 category groups** (not too few, not too many)
✅ **3-6 keywords per category** (comprehensive coverage)
✅ **Cover all major documentation sections**
✅ **Use exact terms from actual docs**
✅ **Include both generic and specific terms**
✅ **No overlap between category keywords**

### Examples

**High Quality:**
```json
{
  "categories": {
    "routing": ["route", "routing", "path", "endpoint", "url"],
    "middleware": ["middleware", "interceptor", "handler", "context"],
    "validation": ["validate", "schema", "validator", "sanitize"]
  }
}
```

**Low Quality:**
```json
{
  "categories": {
    "basic": ["basic", "start"],  // Too vague
    "other": ["other", "misc"]    // Catch-all is bad
  }
}
```

### Category Selection Strategy

1. **Examine the documentation** structure first
2. **Identify major sections** (getting started, API, guides, etc.)
3. **Extract common keywords** from URLs and headings
4. **Group related concepts** together
5. **Test with actual documentation** URLs to verify coverage

---

## Selector Quality

### Excellent Selectors:

✅ **Use semantic HTML first** (`article`, `main`)
✅ **Have fallbacks** (selector chain)
✅ **Avoid fragile ID selectors**
✅ **Tested against current docs**
✅ **Capture all content** without navigation/ads

### Examples

**High Quality (with fallback chain):**
```json
{
  "selectors": {
    "main_content": "article, main, div[role='main'], .content",
    "title": "h1, article h1, title",
    "code_blocks": "pre code, pre, .highlight"
  }
}
```

**Low Quality (fragile):**
```json
{
  "selectors": {
    "main_content": "#specific-id-123",  // Fragile - breaks if ID changes
    "title": "h1"                         // No fallback
  }
}
```

### Selector Testing

Before finalizing selectors, test them with browser DevTools:

```javascript
// In browser console
document.querySelector('article')
document.querySelector('main')
document.querySelector('div[role="main"]')
```

Choose selectors that:
- Return the main content (not navigation or ads)
- Work consistently across all documentation pages
- Are unlikely to change with site redesigns

---

## Description Quality

### Excellent Descriptions:

✅ **Explain WHEN to use the skill**
✅ **List key capabilities covered**
✅ **Mention version if applicable**
✅ **Include unique features**
✅ **1-3 sentences** (concise but informative)

### Examples

**High Quality:**
```
"Use when working with React, including hooks, components, state management, and modern React patterns. Covers React 18+ features including Concurrent Mode, Suspense, and Server Components."
```

**Low Quality:**
```
"React framework documentation"  // Too vague, doesn't explain capabilities
```

### Description Template

```
"[Framework/Tool] for [primary use case]. Use for [key feature 1], [key feature 2], [key feature 3], and [general category]. [Optional: Covers version X+ features including [unique capabilities]]."
```

---

## Rate Limit Guidelines

### Recommended Values by Site Type

| Site Type | Rate Limit | Rationale |
|-----------|------------|-----------|
| Large open source docs (React, Vue, Django) | 0.3-0.5s | Well-resourced servers, generous limits |
| Official vendor docs (Tailwind, FastAPI) | 0.5s | Balanced approach |
| Partner/commercial docs (Steam) | 0.7s | More conservative, respect resources |
| Small project docs | 0.3s | Usually lightweight servers |

### Principles

- **Be respectful** of server resources
- **Avoid rate limiting** issues
- **Balance speed** vs courtesy
- **Test with dry-run** before full scrape

---

## URL Pattern Guidelines

### Include Patterns

✅ **Be specific** to documentation sections
✅ **Use path prefixes** (`/docs/`, `/api/`, `/guide/`)
✅ **Version-aware** when needed (`/v2/`, `/latest/`)

**Examples:**
```json
{
  "include": [
    "/docs/",
    "/api/",
    "/guide/",
    "/tutorial/"
  ]
}
```

### Exclude Patterns

✅ **Remove navigation/utility pages** (`/search`, `/_static/`)
✅ **Exclude blog/marketing** (`/blog/`, `/news/`)
✅ **Remove generated content** (`/genindex.html`)
✅ **Skip changelog** unless relevant (`/changelog/`, `/release-notes/`)

**Examples:**
```json
{
  "exclude": [
    "/search/",
    "/blog/",
    "/_static/",
    "/_images/",
    "/genindex.html"
  ]
}
```

### Common Patterns to Exclude

- Search pages: `/search`, `/search.html`
- Static assets: `/_static/`, `/_images/`, `/img/`, `/js/`, `/css/`
- Generated indexes: `/genindex.html`, `/py-modindex.html`
- Navigation: `/sitemap/`, `/index/`
- Marketing: `/blog/`, `/news/`, `/press/`, `/about/`
- Community: `/forum/`, `/community/`, `/discuss/`

---

## Quality Metrics

### Config Quality Levels

#### HIGH Quality (Production Ready)
- ✅ 5-13 comprehensive categories
- ✅ Multiple start_urls covering key sections
- ✅ Selector fallback chains
- ✅ Appropriate rate limits
- ✅ Well-tuned URL patterns
- ✅ Clear, detailed description
- ✅ Tested and validated

**Examples:** kubernetes.json, godot.json, django.json

#### MEDIUM Quality (Functional but Improvable)
- ⚠️ 3-6 categories (could expand)
- ⚠️ Single or few start_urls
- ⚠️ Basic selectors (no fallbacks)
- ⚠️ Generic URL patterns
- ⚠️ Basic description

**Examples:** vue.json (before enhancement), tailwind.json (before enhancement)

#### LOW Quality (Needs Fixes)
- ❌ Empty or minimal categories
- ❌ No start_urls
- ❌ Fragile selectors
- ❌ Missing URL patterns
- ❌ Placeholder URLs

**Examples:** hono.json (before fix), test-manual.json (before fix)

### Success Criteria Checklist

Before marking a config as HIGH quality, verify:

- [ ] Categories cover all major documentation sections
- [ ] Each category has 3-6 relevant keywords
- [ ] Selectors use semantic HTML with fallbacks
- [ ] Description explains when to use (50+ characters)
- [ ] Rate limit is appropriate for server type
- [ ] URL patterns are specific and tested
- [ ] max_pages is appropriate for documentation size
- [ ] start_urls cover key documentation entry points
- [ ] Config validated with dry-run test
- [ ] No placeholder URLs or paths

---

## Config Template

Use this template when creating new configs:

```json
{
  "name": "framework-name",
  "description": "[Framework] for [use case]. Use for [features]. Covers [version]+ including [capabilities].",
  "base_url": "https://docs.example.com/",
  "start_urls": [
    "https://docs.example.com/getting-started",
    "https://docs.example.com/api",
    "https://docs.example.com/guide"
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
    "api_reference": ["api", "reference", "method", "function"],
    "guides": ["guide", "tutorial", "walkthrough"],
    "advanced": ["advanced", "optimization", "performance"]
  },
  "rate_limit": 0.5,
  "max_pages": 300
}
```

---

## Maintenance Guidelines

### When to Update a Config

- Documentation site redesign (selectors may break)
- New major version released (add new categories)
- Documentation structure changes (update URL patterns)
- Community feedback (improve based on usage)

### Testing Changes

Always test config changes with dry-run mode:

```bash
skill-seekers scrape --config configs/your-config.json --dry-run
```

Verify:
- Selectors extract content correctly
- Categories match actual documentation structure
- URL patterns capture desired pages
- No errors or warnings

---

## Quality Examples

### Kubernetes (HIGH Quality)

```json
{
  "name": "kubernetes",
  "description": "Kubernetes container orchestration platform. Use for K8s clusters, deployments, pods, services, networking, storage, configuration, and DevOps tasks.",
  "categories": {
    "getting_started": ["getting-started", "setup", "learning-environment"],
    "concepts": ["concepts", "overview", "architecture"],
    "workloads": ["workloads", "pods", "deployments", "replicaset", "statefulset", "daemonset"],
    "services": ["services", "networking", "ingress", "service"],
    "storage": ["storage", "volumes", "persistent"],
    "configuration": ["configuration", "configmap", "secret"],
    "security": ["security", "rbac", "policies", "authentication"],
    "tasks": ["tasks", "administer", "configure"],
    "tutorials": ["tutorials", "stateless", "stateful"]
  },
  "max_pages": 1000
}
```

**Why it's HIGH quality:**
- 9 comprehensive categories covering all major K8s concepts
- Detailed description listing use cases
- Appropriate max_pages for extensive documentation
- Keywords match actual Kubernetes documentation structure

---

## Contributing Guidelines

When submitting new configs to the official library:

1. **Use the template** as a starting point
2. **Test thoroughly** with dry-run mode
3. **Verify selectors** work on actual documentation
4. **Document your choices** in PR description
5. **Follow quality standards** outlined in this guide
6. **Target HIGH quality** from the start

---

## References

- [Skill Seekers Documentation](https://github.com/yusufkaraaslan/Skill_Seekers)
- [Template Config](official/test-examples/template-example.json)
- [Example HIGH Quality Configs](official/)

---

**Last Updated:** December 22, 2025
**Version:** 1.0
