from django.conf.urls import url
from .views import AddFriend
from .views import ShowFriend
from .views import AddFavorite


urlpatterns = [
    url('add_friend', AddFriend.as_view(), name ='add_friend'),
    url('show_friend', ShowFriend.as_view(), name ='show_friend'),
    url('add_favorite', AddFavorite.as_view(), name ='add_favorite')
]