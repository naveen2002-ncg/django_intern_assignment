from django.core.management.base import BaseCommand
from vendor.models import Vendor
from product.models import Product
from course.models import Course
from certification.models import Certification
from vendor_product_mapping.models import VendorProductMapping
from product_course_mapping.models import ProductCourseMapping
from course_certification_mapping.models import CourseCertificationMapping


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        Vendor.objects.all().delete()
        Product.objects.all().delete()
        Course.objects.all().delete()
        Certification.objects.all().delete()
        
        vendors = [
            Vendor.objects.create(name='TechCorp', code='V001', description='Tech vendor'),
            Vendor.objects.create(name='EduLearn', code='V002', description='Education vendor'),
            Vendor.objects.create(name='CloudBase', code='V003', description='Cloud vendor'),
        ]
        
        products = [
            Product.objects.create(name='Enterprise Suite', code='P001', description='Enterprise solution'),
            Product.objects.create(name='Cloud Platform', code='P002', description='Cloud platform'),
            Product.objects.create(name='Analytics Engine', code='P003', description='Analytics tool'),
            Product.objects.create(name='Mobile SDK', code='P004', description='Mobile development'),
        ]
        
        courses = [
            Course.objects.create(name='Django Fundamentals', code='C001', description='Django basics'),
            Course.objects.create(name='REST API Design', code='C002', description='API design'),
            Course.objects.create(name='Advanced Python', code='C003', description='Python advanced'),
            Course.objects.create(name='Cloud Architecture', code='C004', description='Cloud design'),
        ]
        
        certifications = [
            Certification.objects.create(name='Django Dev Cert', code='CERT001', description='Django certification'),
            Certification.objects.create(name='REST API Specialist', code='CERT002', description='API certification'),
            Certification.objects.create(name='Python Expert', code='CERT003', description='Python certification'),
            Certification.objects.create(name='Cloud Architect', code='CERT004', description='Cloud certification'),
        ]
        
        VendorProductMapping.objects.create(vendor=vendors[0], product=products[0], primary_mapping=True, is_active=True)
        VendorProductMapping.objects.create(vendor=vendors[0], product=products[1], primary_mapping=False, is_active=True)
        VendorProductMapping.objects.create(vendor=vendors[1], product=products[2], primary_mapping=True, is_active=True)
        VendorProductMapping.objects.create(vendor=vendors[2], product=products[3], primary_mapping=True, is_active=True)
        
        ProductCourseMapping.objects.create(product=products[0], course=courses[0], primary_mapping=True, is_active=True)
        ProductCourseMapping.objects.create(product=products[1], course=courses[3], primary_mapping=True, is_active=True)
        ProductCourseMapping.objects.create(product=products[2], course=courses[1], primary_mapping=True, is_active=True)
        ProductCourseMapping.objects.create(product=products[3], course=courses[2], primary_mapping=True, is_active=True)
        
        CourseCertificationMapping.objects.create(course=courses[0], certification=certifications[0], primary_mapping=True, is_active=True)
        CourseCertificationMapping.objects.create(course=courses[1], certification=certifications[1], primary_mapping=True, is_active=True)
        CourseCertificationMapping.objects.create(course=courses[2], certification=certifications[2], primary_mapping=True, is_active=True)
        CourseCertificationMapping.objects.create(course=courses[3], certification=certifications[3], primary_mapping=True, is_active=True)
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
