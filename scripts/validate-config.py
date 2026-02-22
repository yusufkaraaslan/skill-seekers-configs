#!/usr/bin/env python3
"""
Config Validation Script for Skill Seekers Configs

Validates JSON configuration files against quality standards.
Usage:
    python scripts/validate-config.py official/web-frameworks/react.json
    python scripts/validate-config.py official/
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple, Any


class ConfigValidator:
    """Validator for Skill Seekers config files."""
    
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        
    def load_config(self) -> bool:
        """Load and parse the config file."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            return True
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False
        except FileNotFoundError:
            self.errors.append(f"File not found: {self.config_path}")
            return False
    
    def validate_structure(self) -> bool:
        """Validate basic config structure."""
        required_fields = ['name', 'description']
        
        for field in required_fields:
            if field not in self.config:
                self.errors.append(f"Missing required field: '{field}'")
        
        # Check if unified format or simple format
        if 'sources' in self.config:
            self.info.append("Unified format detected (multi-source)")
            return self._validate_unified_format()
        else:
            self.info.append("Simple format detected (single-source)")
            return self._validate_simple_format()
    
    def _validate_simple_format(self) -> bool:
        """Validate simple (single-source) config format."""
        simple_required = ['base_url', 'selectors', 'categories']
        
        for field in simple_required:
            if field not in self.config:
                self.errors.append(f"Simple format missing required field: '{field}'")
        
        return len(self.errors) == 0
    
    def _validate_unified_format(self) -> bool:
        """Validate unified (multi-source) config format."""
        if 'merge_mode' not in self.config:
            self.warnings.append("Unified format should include 'merge_mode' field")
        
        if 'sources' not in self.config or not isinstance(self.config['sources'], list):
            self.errors.append("Unified format requires 'sources' array")
            return False
        
        for i, source in enumerate(self.config['sources']):
            if 'type' not in source:
                self.errors.append(f"Source {i}: Missing 'type' field")
            elif source['type'] not in ['documentation', 'github', 'pdf']:
                self.warnings.append(f"Source {i}: Unusual type '{source['type']}'")
            
            if source.get('type') == 'documentation':
                self._validate_doc_source(source, i)
            elif source.get('type') == 'github':
                self._validate_github_source(source, i)
        
        return len(self.errors) == 0
    
    def _validate_doc_source(self, source: Dict, index: int):
        """Validate documentation source."""
        required = ['base_url', 'selectors', 'categories']
        for field in required:
            if field not in source:
                self.errors.append(f"Documentation source {index}: Missing '{field}'")
    
    def _validate_github_source(self, source: Dict, index: int):
        """Validate GitHub source."""
        if 'repo' not in source:
            self.errors.append(f"GitHub source {index}: Missing 'repo' field")
        elif '/' not in source.get('repo', ''):
            self.warnings.append(f"GitHub source {index}: Repo should be in 'owner/repo' format")
    
    def validate_categories(self) -> bool:
        """Validate categories quality."""
        # For unified configs, categories are inside sources[0]; for simple configs, at top level
        categories = self.config.get('categories', {})
        if not categories and 'sources' in self.config:
            for source in self.config['sources']:
                if source.get('type') == 'documentation' and 'categories' in source:
                    categories = source['categories']
                    break

        if not categories:
            self.errors.append("No categories defined")
            return False
        
        num_categories = len(categories)
        if num_categories < 5:
            self.warnings.append(f"Low category count: {num_categories} (recommend 5-13)")
        elif num_categories > 13:
            self.warnings.append(f"High category count: {num_categories} (recommend 5-13)")
        else:
            self.info.append(f"Good category count: {num_categories}")
        
        for cat_name, keywords in categories.items():
            if len(keywords) < 3:
                self.warnings.append(f"Category '{cat_name}' has only {len(keywords)} keywords (recommend 3-6)")
            elif len(keywords) > 6:
                self.warnings.append(f"Category '{cat_name}' has {len(keywords)} keywords (recommend 3-6)")
            
            # Check for generic names
            if cat_name.lower() in ['basic', 'other', 'misc', 'general']:
                self.warnings.append(f"Category '{cat_name}' is too generic")
        
        return True
    
    def validate_selectors(self) -> bool:
        """Validate CSS selectors."""
        # Get selectors from appropriate location
        selectors = {}
        if 'selectors' in self.config:
            selectors = self.config['selectors']
        elif 'sources' in self.config:
            for source in self.config['sources']:
                if source.get('type') == 'documentation' and 'selectors' in source:
                    selectors = source['selectors']
                    break
        
        if not selectors:
            self.errors.append("No selectors defined")
            return False
        
        if 'main_content' not in selectors:
            self.errors.append("Missing 'main_content' selector")
        
        # Check for fragile selectors
        for name, selector in selectors.items():
            if selector.startswith('#') and ',' not in selector:
                self.warnings.append(f"Selector '{name}' uses fragile ID selector: '{selector}'")
            if ',' in selector:
                self.info.append(f"Selector '{name}' has fallback chain (good)")
        
        return True
    
    def validate_description(self) -> bool:
        """Validate description quality."""
        desc = self.config.get('description', '')
        
        if len(desc) < 50:
            self.warnings.append(f"Description is short ({len(desc)} chars). Recommend 50+ characters explaining when to use.")
        
        if 'use when' not in desc.lower() and 'use for' not in desc.lower():
            self.warnings.append("Description should explain when to use the skill (include 'Use when...' or 'Use for...')")
        
        return True
    
    def validate_rate_limit(self) -> bool:
        """Validate rate limit settings."""
        rate_limit = self.config.get('rate_limit', 0.5)
        
        if rate_limit < 0.1:
            self.warnings.append(f"Rate limit {rate_limit}s may be too aggressive")
        elif rate_limit > 1.0:
            self.warnings.append(f"Rate limit {rate_limit}s is conservative (may be appropriate for partner sites)")
        else:
            self.info.append(f"Rate limit {rate_limit}s is appropriate")
        
        return True
    
    def validate_max_pages(self) -> bool:
        """Validate max_pages setting — max_pages should NOT be set in production configs."""
        max_pages = self.config.get('max_pages')
        if max_pages is not None:
            self.warnings.append(
                f"max_pages {max_pages} is set — remove from production configs (defaults apply automatically)"
            )
        else:
            self.info.append("max_pages not set (correct for production configs)")
        return True
    
    def validate_metadata(self) -> bool:
        """Validate optional metadata."""
        if 'metadata' not in self.config:
            self.info.append("Consider adding metadata block for better discoverability")
            return True
        
        meta = self.config['metadata']
        recommended = ['author', 'language', 'framework_type', 'use_cases', 'related_skills']
        
        for field in recommended:
            if field not in meta:
                self.warnings.append(f"Metadata missing recommended field: '{field}'")
        
        return True
    
    def calculate_quality_score(self) -> Tuple[int, str]:
        """Calculate overall quality score and rating."""
        score = 100
        
        # Deduct for errors
        score -= len(self.errors) * 20
        
        # Deduct for warnings
        score -= len(self.warnings) * 5
        
        # Bonus for metadata
        if 'metadata' in self.config:
            score += 5
        
        # Bonus for unified format
        if 'sources' in self.config:
            score += 5
        
        score = max(0, min(100, score))
        
        if score >= 90:
            rating = "HIGH"
        elif score >= 70:
            rating = "MEDIUM"
        elif score >= 50:
            rating = "LOW"
        else:
            rating = "CRITICAL"
        
        return score, rating
    
    def validate(self) -> bool:
        """Run all validations."""
        if not self.load_config():
            return False
        
        self.validate_structure()
        self.validate_categories()
        self.validate_selectors()
        self.validate_description()
        self.validate_rate_limit()
        self.validate_max_pages()
        self.validate_metadata()
        
        return len(self.errors) == 0
    
    def print_report(self):
        """Print validation report."""
        print(f"\n{'='*70}")
        print(f"Config: {self.config_path}")
        print(f"{'='*70}")
        
        if self.info:
            print("\n✓ INFO:")
            for msg in self.info:
                print(f"  • {msg}")
        
        if self.warnings:
            print("\n⚠ WARNINGS:")
            for msg in self.warnings:
                print(f"  • {msg}")
        
        if self.errors:
            print("\n✗ ERRORS:")
            for msg in self.errors:
                print(f"  • {msg}")
        
        score, rating = self.calculate_quality_score()
        
        print(f"\n{'-'*70}")
        print(f"Quality Score: {score}/100")
        print(f"Rating: {rating}")
        
        if rating == "HIGH":
            print("✓ Config meets HIGH quality standards")
        elif rating == "MEDIUM":
            print("⚠ Config is functional but could be improved")
        elif rating == "LOW":
            print("⚠ Config needs improvements")
        else:
            print("✗ Config has critical issues and needs fixes")
        
        print(f"{'='*70}\n")


def validate_directory(directory: str) -> None:
    """Validate all JSON configs in a directory."""
    path = Path(directory)
    configs = list(path.rglob("*.json"))
    
    print(f"\nFound {len(configs)} config files in {directory}")
    print("=" * 70)
    
    high_quality = 0
    medium_quality = 0
    low_quality = 0
    
    for config_file in sorted(configs):
        validator = ConfigValidator(str(config_file))
        validator.validate()
        validator.print_report()
        
        score, rating = validator.calculate_quality_score()
        if rating == "HIGH":
            high_quality += 1
        elif rating in ["MEDIUM", "LOW"]:
            medium_quality += 1
        else:
            low_quality += 1
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"HIGH Quality:   {high_quality}")
    print(f"MEDIUM Quality: {medium_quality}")
    print(f"Needs Work:     {low_quality}")
    print("=" * 70)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate-config.py <config-file-or-directory>")
        print("\nExamples:")
        print("  python validate-config.py official/web-frameworks/react.json")
        print("  python validate-config.py official/")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if os.path.isfile(target):
        validator = ConfigValidator(target)
        is_valid = validator.validate()
        validator.print_report()
        sys.exit(0 if is_valid else 1)
    elif os.path.isdir(target):
        validate_directory(target)
        sys.exit(0)
    else:
        print(f"Error: {target} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
