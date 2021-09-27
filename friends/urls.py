from django.conf.urls import url
from .views import AddFriend
from .views import ShowFriend


urlpatterns = [
    url('add_friend', AddFriend.as_view(), name ='add_friend'),
    url('show_friend', ShowFriend.as_view(), name ='show_friend')
]