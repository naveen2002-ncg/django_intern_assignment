from rest_framework import serializers
from .models import ProductCourseMapping
from product.models import Product
from course.models import Course


class ProductCourseMappingSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = ProductCourseMapping
        fields = ['id', 'product', 'product_name', 'course', 'course_name', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        product = data.get('product')
        course = data.get('course')
        
        if product and not Product.objects.filter(pk=product.pk).exists():
            raise serializers.ValidationError("Invalid product.")
        if course and not Course.objects.filter(pk=course.pk).exists():
            raise serializers.ValidationError("Invalid course.")
        
        request = self.context.get('request')
        if request and request.method == 'POST':
            if ProductCourseMapping.objects.filter(product=product, course=course).exists():
                raise serializers.ValidationError("This product-course mapping already exists.")
        
        if data.get('primary_mapping'):
            existing = ProductCourseMapping.objects.filter(product=product, primary_mapping=True)
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise serializers.ValidationError("Only one primary mapping per product is allowed.")
        
        return data
