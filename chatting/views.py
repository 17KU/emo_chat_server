from rest_framework.views import APIView
from .models import User_Chat
from .models import Chat
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
            chat_list.append(dict(chat_index = chat.chat_index,
                                  chat_title = chat.chat_title,
                                  chat_other_id = chat.chat_other_id))

        if len(chat_list) > 0:
            return JsonResponse(chat_list, safe=False)
        else:
            return JsonResponse({'code': '0001', 'msg': '채팅 없음'}, status=200)

