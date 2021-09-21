from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user_friend
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class RelationCreateView(APIView):
    def post(self, request):

        user_i = request.data.get('user')