# Generated by Django 3.2.7 on 2021-09-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_friend',
            name='uf_friend_id',
            field=models.CharField(default=False, max_length=255, unique=True),
        ),
    ]
