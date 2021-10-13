import os

from rest_framework.views import APIView
from django.http import JsonResponse
import models

class GetEmotion(APIView):
    def post(self, request):

        message = request.data.get('message')

        dir_path = os.getcwd()
        model_path = os.path.join(dir_path, "\KoBERT")

        emotion = models.predict(message)

        return JsonResponse(emotion)
