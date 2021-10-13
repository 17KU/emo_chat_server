from django.conf.urls import url
from .views import GetImotion

urlpatterns = [
    url('get_emotion', GetImotion.as_view(), name='get_emotion')
]