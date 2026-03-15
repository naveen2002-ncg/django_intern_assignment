from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreateView(APIView):
    """List all vendors or create a new vendor."""

    @swagger_auto_schema(
        operation_description="Retrieve a list of all vendors with optional filters",
        manual_parameters=[openapi.Parameter('is_active', openapi.IN_QUERY, description='Filter by active status', type=openapi.TYPE_BOOLEAN)],
        responses={200: openapi.Response('List of vendors', VendorSerializer(many=True))}
    )
    def get(self, request):
        queryset = Vendor.objects.all()
        is_active = request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        
        serializer = VendorSerializer(queryset, many=True)
        return Response({'count': queryset.count(), 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new vendor",
        request_body=VendorSerializer,
        responses={201: openapi.Response('Vendor created successfully', VendorSerializer), 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = VendorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetailView(APIView):
    """Retrieve, update, or delete a specific vendor."""

    def get_object(self, pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return None

    @swagger_auto_schema(operation_description="Retrieve a specific vendor by ID", responses={200: openapi.Response('Vendor details', VendorSerializer), 404: 'Not found'})
    def get(self, request, pk):
        vendor = self.get_object(pk)
        if not vendor:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update a vendor (full update)", request_body=VendorSerializer, responses={200: openapi.Response('Updated', VendorSerializer), 400: 'Bad Request', 404: 'Not found'})
    def put(self, request, pk):
        vendor = self.get_object(pk)
        if not vendor:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(vendor, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Partially update a vendor", request_body=VendorSerializer, responses={200: openapi.Response('Updated', VendorSerializer), 400: 'Bad Request', 404: 'Not found'})
    def patch(self, request, pk):
        vendor = self.get_object(pk)
        if not vendor:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorSerializer(vendor, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Delete a vendor", responses={204: 'Deleted', 404: 'Not found'})
    def delete(self, request, pk):
        vendor = self.get_object(pk)
        if not vendor:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
