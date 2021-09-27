from MySQLdb import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user_friend
from login_signup.models import User
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.

class AddFriend(APIView):
    def post(self, request):

        user_id = request.data.get('user_id')
        add_friend_id = request.data.get('add_friend_id')


        # 유저 아이디가 올바른지
        try:
            user = User.objects.filter(user_id=user_id).first()
        except User.DoesNotExist:
            return JsonResponse({'code':'0001', 'msg':'아이디가 존재하지 않습니다'}, status=200)

        # 친구 추가할 ID가 User 테이블에 존재하는지
        try:
            User.objects.filter(user_id=add_friend_id)
        except User.DoesNotExist:
            return JsonResponse({'code':'0001','msg':'상대방이 존재하지 않습니다'}, status=200)


        # 친구 추가 하기

        # 친구 추가 아이디가 본인 아이디 와 같으면
        if user_id == add_friend_id:
            return JsonResponse({'code':'0002', 'msg':'본인을 추가할 수 없습니다'}, status=200)

        #criterion1 = Q(uf_user_id=user_id)
        #criterion2 = Q(uf_friend_id=add_friend_id)

        # 원래 친구가 아니면
        friend = user_friend.objects.filter(uf_user_id=user_id,uf_friend_id=add_friend_id).first()

        if friend is None:
            user_friend.objects.create(uf_user_id=user, uf_friend_id=add_friend_id)
            return JsonResponse({'code': '0000', 'mgs': 'success', 'user_id': user_id, 'add_friend_id': add_friend_id},
                                status=200)
        else:
            return JsonResponse({'code':'0003', 'msg':'이미 친구입니다'},status=200)



class ShowFriend(APIView):
    def post(self, request):

        user_id = request.data.get('user_id')

        # 유저 아이디가 올바른지
        try:
            user = User.objects.filter(user_id=user_id)
        except User.DoesNotExist:
            return self.response(message = '잘못된 요청입니다.', status=200)

        # 유저 아이디에 해당하는 친구 목록
        friend = user_friend.objects.filter(uf_user_id=user_id)

        return Response(friend.values())