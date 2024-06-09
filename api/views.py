from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import StreamModel,WatchModel,ReviewModel
from .serializers import StreamSerializer,WatchSerializer,ReviewSerializer
from rest_framework import generics

class StreamList(APIView):
    def post(self, request):
        serializer = StreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self, request):
        streams = StreamModel.objects.all()
        serializer = StreamSerializer(streams, many=True)
        return Response(serializer.data)
    
class StreamDetails(APIView):
    def put(self,request,pk):
        try:
            stream = StreamModel.objects.get(pk=pk)
        except StreamModel.DoesNotExist:
            return Response({"not found"})
        serializer = StreamSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, resquest,pk):
        try:
            stream = StreamModel.objects.get(pk=pk)
        except StreamModel.DoesNotExist:
            return Response({"not found"})
        serializer = StreamSerializer(stream)
        return Response(serializer.data)
    
    def delete(self, resquest,pk):
        try:
            stream = StreamModel.objects.get(pk=pk)
        except StreamModel.DoesNotExist:
            return Response({"not found"})
        stream.delete()
        return Response({"Deleted successfully"})


#watch list views

class WatchListView(APIView):
    def post(self, request):
        data = WatchSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)
    
    def get(self, request):
        watch = WatchModel.objects.all()
        data = WatchSerializer(watch, many=True)
        return Response(data.data)

class WatchDetails(APIView):
    def put(self,request,pk):
        try:
            movie = WatchModel.objects.get(pk=pk)
        except WatchModel.DoesNotExist:
            return Response({"movies not found"})
        data = WatchSerializer(movie, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        return Response(data.errors)
    
    def get(self,request,pk):
        try:
            movie = WatchModel.objects.get(pk=pk)
        except WatchModel.DoesNotExist:
            return Response({"movies not found"})
        data = WatchSerializer(movie)
        return Response(data.data)
    
    def delete(self,request,pk):
        try:
            movie = WatchModel.objects.get(pk=pk)
        except WatchModel.DoesNotExist:
            return Response({"movies not found"})
        movie.delete()
        return Response({"movies deleted successfully"})

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = ReviewModel.objects.all()
    



        
