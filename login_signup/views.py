from rest_framework.views import APIView
from .models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class UserRegist(APIView):
    # APIView에 있는 post() method
    def post(self, request):
        # client로 부터 받은 id와 pw, name 저장
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_pw_encryted = make_password(user_pw)
        user_name = request.data.get('user_name')

        user = User.objects.filter(user_id = user_id).first()
        if user is not None:
            return JsonResponse({'code': '0001', 'msg': '동일한 아이디 존재'}, status=200)

        User.objects.create(user_id = user_id, user_pw = user_pw_encryted, user_name = user_name)

        return JsonResponse({'code': '0000', 'msg': '회원가입 성공'}, status=200)

class UserLogin(APIView):
    # APIView에 있는 post() method
    def post(self, request):
        # client로 부터 받은 id와 pw 저장
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = User.objects.filter(user_id = user_id).first()

        if user is None:
            return JsonResponse({'code': '0001', 'msg': '로그인 실패, 아이디 틀림', 'user_id': None, 'user_name': None}, status=200)

        if check_password(user_pw, user.user_pw) :
            return JsonResponse({'code': '0000', 'msg': '로그인 성공', 'user_id': user.user_id, 'user_name': user.user_name}, status=200)
        else:
            return JsonResponse({'code': '0002', 'msg': '로그인 실패, 비밀번호 틀림', 'user_id': None, 'user_name': None}, status=200)