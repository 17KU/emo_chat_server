from django.conf.urls import url
from .views import UserRegist
from .views import UserLogin


urlpatterns = [
    url('user_regist', UserRegist.as_view(), name = 'user_regist'),
    url('user_login', UserLogin.as_view(), name = 'user_login')
]