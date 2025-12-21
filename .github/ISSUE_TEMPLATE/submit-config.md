---
name: Submit Config
about: Submit a new configuration file for Skill Seekers
title: '[CONFIG] '
labels: 'config-submission, needs-review'
assignees: ''
---

## Config Submission

### Framework/Tool Name
<!-- Example: Svelte, Ruby on Rails, TensorFlow, etc. -->

### Category
<!-- Select one: web-frameworks, game-engines, devops, css-frameworks, development-tools, gaming, other -->

### Configuration JSON
```json
{
  "name": "",
  "description": "",
  "base_url": "",
  "selectors": {
    "main_content": "",
    "title": "",
    "code_blocks": ""
  },
  "url_patterns": {
    "include": [],
    "exclude": []
  },
  "categories": {

  },
  "rate_limit": 0.5,
  "max_pages": 100
}
```

### Testing Results
<!-- Paste output from `skill-seekers estimate` and test scraping results -->

**Estimated Pages:**
```
<!-- Output from estimate command -->
```

**Test Scraping:**
```
<!-- Results from scraping with max_pages: 10-20 -->
```

### Documentation URL
<!-- Link to official documentation website -->

### Additional Notes
<!-- Any special considerations, limitations, or recommendations -->

---

### Checklist
- [ ] Config tested with `skill-seekers estimate`
- [ ] Config tested with limited scraping (10-20 pages)
- [ ] Selectors extract content correctly
- [ ] URL patterns work as expected
- [ ] No rate limiting issues observed
- [ ] Config follows naming conventions (lowercase, hyphens)

---

**Maintainer Notes:**
<!-- This section will be filled by maintainers during review -->
- [ ] Config validated
- [ ] Test scraping completed
- [ ] Added to appropriate category
- [ ] API updated
