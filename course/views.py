from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Course
from .serializers import CourseSerializer


class CourseListCreateView(APIView):
    @swagger_auto_schema(responses={200: openapi.Response('List', CourseSerializer(many=True))})
    def get(self, request):
        queryset = Course.objects.all()
        is_active = request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        serializer = CourseSerializer(queryset, many=True)
        return Response({'count': queryset.count(), 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CourseSerializer, responses={201: openapi.Response('Created', CourseSerializer)})
    def post(self, request):
        serializer = CourseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(CourseSerializer(obj).data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(obj, data=request.data, partial=True, context={'request': request})
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
