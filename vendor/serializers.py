from rest_framework import serializers
from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'code', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_code(self, value):
        request = self.context.get('request')
        if request and request.method == 'PUT':
            if Vendor.objects.filter(code=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("A vendor with this code already exists.")
        elif request and request.method == 'POST':
            if Vendor.objects.filter(code=value).exists():
                raise serializers.ValidationError("A vendor with this code already exists.")
        return value
