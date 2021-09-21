from MySQLdb import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user_friend
from login_signup.models import User
from django.http import JsonResponse

# Create your views here.

class AddFriend(APIView):
    def post(self, request):

        user_id = request.data.get('user_id')
        add_friend_id = request.data.get('add_friend_id')


        # 유저 아이디가 올바른지
        try:
            user = User.objects.filter(user_id=user_id)
        except User.DoesNotExist:
            return self.response(message = '잘못된 요청입니다.', status=200)


        # 친구 추가할 ID가 User 테이블에 존재하는지
        try:
            User.objects.filter(user_id=add_friend_id)
        except User.DoesNotExist:
            return self.response(message = '잘못된 요청입니다.', status=200)

        # 친구 추가 하기

        # 친구 추가 아이디가 본인 아이디 와 같으면
        if user_id == add_friend_id:
            raise IntegrityError

        # 원래 친구가 아니면
        friend = user_friend.objects.filter(user_id=user_id, friend_id=add_friend_id)
        if friend is not None:
            user_friend.objects.create(user_id=user.user_id, friend_id=add_friend_id)

        data = dict(
            user_id = user_id,
            friend_id = add_friend_id
        )

        return Response(data)


class ShowFriend(APIView):
    def post(self, request):

        user_id = request.data.get('user_id')


        data = dict(
            user_id = user_id
        )

        return Response(data)