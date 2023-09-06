import os

from django.conf import settings
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from.serializers import VideoSerializer
from rest_framework.response import Response
from .retina_video_extraction import process_video_and_predict

api_key = 'TVZxyhQ0qA0Yztn1SjaF'

class VideoAdd(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = VideoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data["video"]
            p = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            serializer.save()
            # Call function

            output = process_video_and_predict(p, api_key)
            print(output)

            return Response(
                output,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        