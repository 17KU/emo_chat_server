from django.conf.urls import url
from .views import ChatListSelect

urlpatterns = [
    url('chat_list_select', ChatListSelect.as_view(), name = 'chat_list_select'),
]