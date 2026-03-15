from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer


class VendorProductMappingListCreateView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('vendor_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('product_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('is_active', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
        ],
        responses={200: openapi.Response('List', VendorProductMappingSerializer(many=True))}
    )
    def get(self, request):
        queryset = VendorProductMapping.objects.select_related('vendor', 'product').all()
        if request.query_params.get('vendor_id'):
            queryset = queryset.filter(vendor_id=request.query_params['vendor_id'])
        if request.query_params.get('product_id'):
            queryset = queryset.filter(product_id=request.query_params['product_id'])
        if request.query_params.get('is_active'):
            queryset = queryset.filter(is_active=request.query_params['is_active'].lower() == 'true')
        serializer = VendorProductMappingSerializer(queryset, many=True)
        return Response({'count': queryset.count(), 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=VendorProductMappingSerializer, responses={201: openapi.Response('Created', VendorProductMappingSerializer)})
    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorProductMappingDetailView(APIView):
    def get_object(self, pk):
        try:
            return VendorProductMapping.objects.select_related('vendor', 'product').get(pk=pk)
        except VendorProductMapping.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(VendorProductMappingSerializer(obj).data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorProductMappingSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorProductMappingSerializer(obj, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
