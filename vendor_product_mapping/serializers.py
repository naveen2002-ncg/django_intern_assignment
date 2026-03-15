from rest_framework import serializers
from .models import VendorProductMapping
from vendor.models import Vendor
from product.models import Product


class VendorProductMappingSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = VendorProductMapping
        fields = ['id', 'vendor', 'vendor_name', 'product', 'product_name', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        vendor = data.get('vendor')
        product = data.get('product')
        
        if vendor and not Vendor.objects.filter(pk=vendor.pk).exists():
            raise serializers.ValidationError("Invalid vendor.")
        if product and not Product.objects.filter(pk=product.pk).exists():
            raise serializers.ValidationError("Invalid product.")
        
        request = self.context.get('request')
        if request and request.method == 'POST':
            if VendorProductMapping.objects.filter(vendor=vendor, product=product).exists():
                raise serializers.ValidationError("This vendor-product mapping already exists.")
        
        if data.get('primary_mapping'):
            existing = VendorProductMapping.objects.filter(vendor=vendor, primary_mapping=True)
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise serializers.ValidationError("Only one primary mapping per vendor is allowed.")
        
        return data
