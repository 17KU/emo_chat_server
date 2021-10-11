from rest_framework.views import APIView
from .models import User_Chat
from .models import Chat
from login_signup.models import User
from friends.models import user_friend
from django.http import JsonResponse


# Create your views here.

class ChatListSelect(APIView):
    # APIView에 있는 post() method
    def post(self, request):
        # client로 부터 받은 user_id 저장
        user_id = request.data.get('user_id')

        # User_Chat 테이블에서 해당하는 유저의 모든 chat_index를 가지고 옴
        uc_chat_index_list = []
        user_chat_list = User_Chat.objects.filter(uc_user_id=user_id).all()
        for user_chat in user_chat_list:
            uc_chat_index_list.append(user_chat.uc_chat_index)

        # chat_index를 통해 채팅방 목록을 가지고 옴
        chat_list = []
        for uc_chat_index in uc_chat_index_list:
            chat = Chat.objects.filter(chat_index=uc_chat_index.chat_index).first()
            chat_list.append(dict(chat_index=chat.chat_index,
                                  chat_title=chat.chat_title,
                                  chat_other_id=chat.chat_other_id))

        if len(chat_list) > 0:
            return JsonResponse(chat_list, safe=False)
        else:
            return JsonResponse({'code': '0001', 'msg': '채팅 없음'}, status=200)


class ChatListInsert(APIView):
    # APIView에 있는 post() method
    def post(self, request):
        # client로 부터 받은 user_id, friend_id 저장
        user_id = request.data.get('user_id')
        friend_id = request.data.get('friend_id')

        friend = user_friend.objects.filter(uf_user_id = user_id, uf_friend_id = friend_id).first()

        #친구 관계인지 확인
        if friend is not None:
            uc_chat_list = User_Chat.objects.filter(uc_user_id = user_id).all()
            for uc_chat in uc_chat_list:
                chat = Chat.objects.filter(chat_index = uc_chat.uc_chat_index.chat_index).first()
                if (chat is not None) and (chat.chat_other_id == friend_id):
                    return JsonResponse({'code': '0002', 'msg': '이미 존재하는 채팅방 입니다.'}, status=200)

            friend_name = User.objects.filter(user_id = friend_id).first().user_name
            new_chat = Chat.objects.create(chat_title = friend_name, chat_other_id = friend_id)
            User_Chat.objects.create(uc_chat_index = new_chat.chat_index, uc_user_id = user_id)

        else:
            return JsonResponse({'code': '0001', 'msg': '서로 친구 관계가 아닙니다.'}, status=200)




