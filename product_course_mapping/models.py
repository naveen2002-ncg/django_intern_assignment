from django.db import models
from product.models import Product
from course.models import Course
from django.core.exceptions import ValidationError


class ProductCourseMapping(models.Model):
    """Mapping between Product and Course."""
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='course_mappings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='product_mappings')
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'course')
        ordering = ['-created_at']
        indexes = [models.Index(fields=['product', 'is_active']), models.Index(fields=['course', 'is_active'])]

    def clean(self):
        if self.primary_mapping:
            existing = ProductCourseMapping.objects.filter(product=self.product, primary_mapping=True).exclude(pk=self.pk)
            if existing.exists():
                raise ValidationError("Only one primary mapping per product is allowed.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} -> {self.course.name}"
