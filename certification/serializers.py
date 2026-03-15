from rest_framework import serializers
from .models import Certification


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'name', 'code', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_code(self, value):
        request = self.context.get('request')
        if request and request.method == 'PUT':
            if Certification.objects.filter(code=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("A certification with this code already exists.")
        elif request and request.method == 'POST':
            if Certification.objects.filter(code=value).exists():
                raise serializers.ValidationError("A certification with this code already exists.")
        return value
