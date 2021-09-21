from django.db import models


# Create your models here.

class user_friend(models.Model):

    user_id = models.AutoField(primary_key=True)
    friend_id = models.IntegerField()

    class Meta :
        db_table = 'user_friend'
        verbose_name = '친구목록'
