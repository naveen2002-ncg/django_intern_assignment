import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.test import Client

client = Client()

print("Testing API Endpoints")
print("=" * 60)

endpoints = [
    ('/api/vendors/', 'GET'),
    ('/api/products/', 'GET'),
    ('/api/courses/', 'GET'),
    ('/api/certifications/', 'GET'),
    ('/api/vendor-product-mappings/', 'GET'),
    ('/api/product-course-mappings/', 'GET'),
    ('/api/course-certification-mappings/', 'GET'),
]

for url, method in endpoints:
    response = client.get(url)
    print(f"\n{method} {url}")
    print(f"  Status: {response.status_code}")
    if response.status_code == 200:
        try:
            data = json.loads(response.content)
            count = data.get('count', 'N/A')
            print(f"  Count: {count}")
            print(f"  ✓ SUCCESS")
        except:
            print(f"  Response: {response.content[:100]}")
    else:
        print(f"  Error: {response.content[:200]}")
