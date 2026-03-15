import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.urls import get_resolver

def show_urls(urlpatterns, prefix=""):
    for pattern in urlpatterns:
        full_pattern = prefix + str(pattern.pattern)
        print(f"{full_pattern}")
        if hasattr(pattern, 'url_patterns'):
            show_urls(pattern.url_patterns, full_pattern)

resolver = get_resolver()
print("All URL Patterns:")
show_urls(resolver.url_patterns)
