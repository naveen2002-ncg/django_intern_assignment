from django.db import models
from course.models import Course
from certification.models import Certification
from django.core.exceptions import ValidationError


class CourseCertificationMapping(models.Model):
    """Mapping between Course and Certification."""
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certification_mappings')
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='course_mappings')
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('course', 'certification')
        ordering = ['-created_at']
        indexes = [models.Index(fields=['course', 'is_active']), models.Index(fields=['certification', 'is_active'])]

    def clean(self):
        if self.primary_mapping:
            existing = CourseCertificationMapping.objects.filter(course=self.course, primary_mapping=True).exclude(pk=self.pk)
            if existing.exists():
                raise ValidationError("Only one primary mapping per course is allowed.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.name} -> {self.certification.name}"
