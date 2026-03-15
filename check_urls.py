import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.urls import get_resolver

resolver = get_resolver()
print("URL Patterns:")
for pattern in resolver.url_patterns:
    print(f"  {pattern.pattern}")
