#!/usr/bin/env python
"""Script to create remaining views, urls, and admin files"""
import os

# Generic APIView template for master apps
MASTER_VIEW_TEMPLATE = '''from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import {Model}
from .serializers import {Model}Serializer


class {Model}ListCreateView(APIView):
    """List all {model_lower} or create a new {model_lower}."""

    @swagger_auto_schema(
        operation_description="Retrieve a list of all {model_lower}s",
        manual_parameters=[openapi.Parameter('is_active', openapi.IN_QUERY, description='Filter by active status', type=openapi.TYPE_BOOLEAN)],
        responses={{200: openapi.Response('List', {Model}Serializer(many=True))}}
    )
    def get(self, request):
        queryset = {Model}.objects.all()
        is_active = request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        serializer = {Model}Serializer(queryset, many=True)
        return Response({{'count': queryset.count(), 'data': serializer.data}}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body={Model}Serializer, responses={{201: openapi.Response('Created', {Model}Serializer)}})
    def post(self, request):
        serializer = {Model}Serializer(data=request.data, context={{'request': request}})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class {Model}DetailView(APIView):
    """Retrieve, update, or delete a specific {model_lower}."""

    def get_object(self, pk):
        try:
            return {Model}.objects.get(pk=pk)
        except {Model}.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({{'error': '{Model} not found'}}, status=status.HTTP_404_NOT_FOUND)
        serializer = {Model}Serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({{'error': '{Model} not found'}}, status=status.HTTP_404_NOT_FOUND)
        serializer = {Model}Serializer(obj, data=request.data, context={{'request': request}})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({{'error': '{Model} not found'}}, status=status.HTTP_404_NOT_FOUND)
        serializer = {Model}Serializer(obj, data=request.data, partial=True, context={{'request': request}})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({{'error': '{Model} not found'}}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

# URL template
URL_TEMPLATE_MASTER = '''from django.urls import path
from .views import {Model}ListCreateView, {Model}DetailView

urlpatterns = [
    path('{url_name}/', {Model}ListCreateView.as_view(), name='{url_name}-list-create'),
    path('{url_name}/<int:pk>/', {Model}DetailView.as_view(), name='{url_name}-detail'),
]
'''

# Admin template
ADMIN_TEMPLATE = '''from django.contrib import admin
from .models import {Model}


@admin.register({Model})
class {Model}Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'code']
    readonly_fields = ['created_at', 'updated_at']
'''

# Generate files for master apps
master_apps = {
    'product': 'Product',
    'course': 'Course',
    'certification': 'Certification'
}

print("Master views template ready. Use it to create remaining views if needed.")
