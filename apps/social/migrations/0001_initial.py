# Generated by Django 5.0.6 on 2024-06-18 06:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('caption', models.TextField(verbose_name='Описание')),
                ('hashtag', models.CharField(max_length=128, verbose_name='Хештэг')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пост',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('text', models.TextField()),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='social.post')),
            ],
            options={
                'verbose_name': 'Комменты',
                'verbose_name_plural': 'Коменты',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('website', models.URLField()),
                ('followers', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='images/')),
                ('expires_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user5', to='social.userprofile')),
            ],
            options={
                'verbose_name': 'Сторис',
                'verbose_name_plural': 'Сторис',
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='social.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='social.userprofile')),
            ],
            options={
                'verbose_name': 'Лайки на пост',
                'verbose_name_plural': 'Лайки на пост',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(to='social.userprofile'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='social.userprofile'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('join_key', models.CharField(blank=True, max_length=32, null=True)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='social.userprofile')),
                ('members', models.ManyToManyField(to='social.userprofile')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группа',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('followerUp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followerUp', to='social.userprofile')),
                ('followingUP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follofingUp', to='social.userprofile')),
            ],
            options={
                'verbose_name': 'Подписки',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='social.comment')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user4', to='social.userprofile')),
            ],
            options={
                'verbose_name': 'Лайк на коммент',
                'verbose_name_plural': 'Лайк на коммент',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user3', to='social.userprofile'),
        ),
    ]
