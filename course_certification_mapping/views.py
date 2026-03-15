from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreateView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('course_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('certification_id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('is_active', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
        ],
        responses={200: openapi.Response('List', CourseCertificationMappingSerializer(many=True))}
    )
    def get(self, request):
        queryset = CourseCertificationMapping.objects.select_related('course', 'certification').all()
        if request.query_params.get('course_id'):
            queryset = queryset.filter(course_id=request.query_params['course_id'])
        if request.query_params.get('certification_id'):
            queryset = queryset.filter(certification_id=request.query_params['certification_id'])
        if request.query_params.get('is_active'):
            queryset = queryset.filter(is_active=request.query_params['is_active'].lower() == 'true')
        serializer = CourseCertificationMappingSerializer(queryset, many=True)
        return Response({'count': queryset.count(), 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer, responses={201: openapi.Response('Created', CourseCertificationMappingSerializer)})
    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailView(APIView):
    def get_object(self, pk):
        try:
            return CourseCertificationMapping.objects.select_related('course', 'certification').get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(CourseCertificationMappingSerializer(obj).data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseCertificationMappingSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseCertificationMappingSerializer(obj, data=request.data, partial=True, context={'request': request})
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
