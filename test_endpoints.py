#!/usr/bin/env python
"""Test script to verify API endpoints"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.urls import reverse, get_resolver
from django.test import Client

client = Client()

print("=" * 60)
print("Testing API Endpoints")
print("=" * 60)

# Get all URLs
resolver = get_resolver()
print("\nRegistered URL Patterns:")
for pattern in resolver.url_patterns:
    print(f"  {pattern.pattern}")

print("\n" + "=" * 60)
print("Testing Endpoints:")
print("=" * 60)

test_urls = [
    '/api/vendors/',
    '/api/vendors/1/',
    '/api/products/',
    '/api/courses/',
    '/api/certifications/',
    '/api/vendor-product-mappings/',
    '/api/product-course-mappings/',
    '/api/course-certification-mappings/',
    '/swagger/',
    '/redoc/',
]

for url in test_urls:
    try:
        response = client.get(url)
        status = "✓" if response.status_code < 400 else "✗"
        print(f"{status} GET {url:<40} -> {response.status_code}")
    except Exception as e:
        print(f"✗ GET {url:<40} -> ERROR: {str(e)}")

print("\n" + "=" * 60)
