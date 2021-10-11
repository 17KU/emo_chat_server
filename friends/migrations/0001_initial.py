# Generated by Django 3.2.7 on 2021-09-29 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf_friend_id', models.CharField(default=False, max_length=255)),
                ('uf_favorite', models.BooleanField(default='False')),
                ('uf_user_id', models.ForeignKey(db_column='uf_user_id', default=False, on_delete=django.db.models.deletion.CASCADE, to='login_signup.user')),
            ],
            options={
                'verbose_name': '친구목록',
                'db_table': 'user_friend',
            },
        ),
    ]
