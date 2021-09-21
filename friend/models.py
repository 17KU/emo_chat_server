from django.db import models
from login_signup.models import User

# Create your models here.

class user_friend(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_id', null=False, default = False)
    friend_id = models.CharField(max_length=64, unique=True, null=False, default=False)

    class Meta :
        db_table = 'user_friend'
        verbose_name = '친구목록'
