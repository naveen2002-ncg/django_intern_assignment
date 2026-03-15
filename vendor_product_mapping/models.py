from django.db import models
from vendor.models import Vendor
from product.models import Product
from django.core.exceptions import ValidationError


class VendorProductMapping(models.Model):
    """Mapping between Vendor and Product."""
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='product_mappings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='vendor_mappings')
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('vendor', 'product')
        ordering = ['-created_at']
        indexes = [models.Index(fields=['vendor', 'is_active']), models.Index(fields=['product', 'is_active'])]

    def clean(self):
        if self.primary_mapping:
            existing = VendorProductMapping.objects.filter(vendor=self.vendor, primary_mapping=True).exclude(pk=self.pk)
            if existing.exists():
                raise ValidationError("Only one primary mapping per vendor is allowed.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.vendor.name} -> {self.product.name}"
