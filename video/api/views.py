from rest_framework.decorators import api_view
from rest_framework.response import Response
from video.models import Video
from .serializers import VideoSerializer
from rest_framework import status


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/videos',
        'POST /api/add',
        'POST /api/delete/<str:pk>'
    ]

    return Response(routes)


@api_view(['GET'])
def getVideos(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addVideo(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def deleteVideo(request, pk):
    video = Video.objects.get(id=pk)
    if request.method == 'POST':
        video.delete()

    return Response({'error':'Deleted'}, status=status.HTTP_200_OK)

    