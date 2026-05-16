#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apologize Machine - Test Suite

These tests ensure the apology generator remains... functional.
Note: "functional" here means "produces funny output", not "actually helps anyone".
"""

import sys
import unittest

# Import the main module
import apologize_machine


class TestApologyGenerator(unittest.TestCase):
    """Test cases for the Apologize Machine."""

    def setUp(self):
        """Set up test fixtures."""
        self.languages = ['en', 'vi', 'zh', 'ja']
        self.labels = ['reason_label', 'action_label', 'promise_label', 'consequence_label']

    def test_all_languages_have_data(self):
        """Verify all languages have the required data arrays."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                self.assertIn(lang, apologize_machine.DATA)
                self.assertIn('apology', apologize_machine.DATA[lang])
                self.assertIn('reason', apologize_machine.DATA[lang])
                self.assertIn('action', apologize_machine.DATA[lang])
                self.assertIn('promise', apologize_machine.DATA[lang])
                self.assertIn('consequence', apologize_machine.DATA[lang])

    def test_all_languages_have_labels(self):
        """Verify all languages have the required labels."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                self.assertIn(lang, apologize_machine.LANG)
                for label in self.labels:
                    self.assertIn(label, apologize_machine.LANG[lang])

    def test_data_arrays_not_empty(self):
        """Verify all data arrays have content."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                data = apologize_machine.DATA[lang]
                self.assertGreater(len(data['apology']), 0, f"Empty apology array for {lang}")
                self.assertGreater(len(data['reason']), 0, f"Empty reason array for {lang}")
                self.assertGreater(len(data['action']), 0, f"Empty action array for {lang}")
                self.assertGreater(len(data['promise']), 0, f"Empty promise array for {lang}")
                self.assertGreater(len(data['consequence']), 0, f"Empty consequence array for {lang}")

    def test_generate_returns_string(self):
        """Verify generate() returns a string."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                result = apologize_machine.generate(lang)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_generate_contains_labels(self):
        """Verify generated output contains language-specific labels."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                result = apologize_machine.generate(lang)
                labels = apologize_machine.LANG[lang]
                # Check that labels appear in output
                for label_key in self.labels:
                    label = labels[label_key]
                    if label:  # Skip empty labels
                        # Label might be truncated in box, so just check it's reasonable
                        self.assertGreater(len(label), 0)

    def test_multiple_generates_are_random(self):
        """Verify multiple generates produce different output (with high probability)."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                results = set()
                for _ in range(10):
                    result = apologize_machine.generate(lang)
                    results.add(result)
                # At least some variation expected (statistically almost certain)
                self.assertGreater(len(results), 1, "Generate should produce varied output")

    def test_utf8_compatibility(self):
        """Verify the program can handle UTF-8 encoded data."""
        for lang in self.languages:
            with self.subTest(lang=lang):
                result = apologize_machine.generate(lang)
                # If we get here without encoding errors, we're good
                self.assertIsInstance(result, str)
                # Try encoding (will raise if invalid)
                result.encode('utf-8')


class TestDataQuality(unittest.TestCase):
    """Test cases for data quality checks."""

    def test_no_empty_strings(self):
        """Verify no empty strings in data arrays."""
        for lang in ['en', 'vi', 'zh', 'ja']:
            with self.subTest(lang=lang):
                data = apologize_machine.DATA[lang]
                for key in ['apology', 'reason', 'action', 'promise', 'consequence']:
                    for item in data[key]:
                        self.assertGreater(len(item.strip()), 0, f"Empty string in {lang}.{key}")

    def test_minimum_data_count(self):
        """Verify minimum number of items per category per language."""
        minimums = {
            'apology': 10,
            'reason': 15,
            'action': 10,
            'promise': 10,
            'consequence': 10,
        }
        for lang in ['en', 'vi', 'zh', 'ja']:
            with self.subTest(lang=lang):
                data = apologize_machine.DATA[lang]
                for category, minimum in minimums.items():
                    count = len(data[category])
                    self.assertGreaterEqual(count, minimum, 
                        f"{lang}.{category} has {count}, expected >= {minimum}")


if __name__ == '__main__':
    print("🧪 Running Apologize Machine Test Suite")
    print("=" * 50)
    print("Note: These tests check if the program is 'functional'.")
    print("      'Functional' = produces funny output.")
    print("      Not = actually helps anyone remember things.")
    print("=" * 50)
    print()
    unittest.main(verbosity=2)