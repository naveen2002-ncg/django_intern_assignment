from rest_framework import serializers
from .models import CourseCertificationMapping
from course.models import Course
from certification.models import Certification


class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    certification_name = serializers.CharField(source='certification.name', read_only=True)

    class Meta:
        model = CourseCertificationMapping
        fields = ['id', 'course', 'course_name', 'certification', 'certification_name', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        course = data.get('course')
        certification = data.get('certification')
        
        if course and not Course.objects.filter(pk=course.pk).exists():
            raise serializers.ValidationError("Invalid course.")
        if certification and not Certification.objects.filter(pk=certification.pk).exists():
            raise serializers.ValidationError("Invalid certification.")
        
        request = self.context.get('request')
        if request and request.method == 'POST':
            if CourseCertificationMapping.objects.filter(course=course, certification=certification).exists():
                raise serializers.ValidationError("This course-certification mapping already exists.")
        
        if data.get('primary_mapping'):
            existing = CourseCertificationMapping.objects.filter(course=course, primary_mapping=True)
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise serializers.ValidationError("Only one primary mapping per course is allowed.")
        
        return data
