from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    bio = models.CharField(max_length=128)
    image= models.ImageField(blank=True,null=True,upload_to='images/')
    website=models.URLField()
    followers=models.IntegerField()
    def __str__(self):
        return f'{self.user} {self.bio}'

    class Meta:
        verbose_name = _('Профиль')
        verbose_name_plural = _('Профиль')

class Follow(models.Model):
    followerUp=models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='followerUp')
    followingUP=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='follofingUp')
    created_at=models.DateTimeField(auto_created=True,verbose_name='Дата создания')
    def __str__(self):
        return f'{self.followerUp} {self.followingUP}'


    class Meta:
        verbose_name = _('Подписки')
        verbose_name_plural = _('Подписки')
class Post(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='user1')
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    caption=models.TextField(verbose_name='Описание')
    created_at=models.DateTimeField(auto_created=True,verbose_name='Дата создания')
    likes=models.ManyToManyField(UserProfile)
    hashtag=models.CharField(max_length=128,verbose_name='Хештэг')

    def __str__(self):
        return f'{self.user} {self.hashtag}'


    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Пост')
class PostLike(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='user2')
    post = models.OneToOneField(Post,on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_created=True,verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user} {self.post}'

    class Meta:
        verbose_name = _('Лайки на пост')
        verbose_name_plural = _('Лайки на пост')
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post')
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='user3')
    text = models.TextField()
    created_at=models.DateTimeField(auto_created=True,verbose_name='Дата создания')
    post = models.OneToOneField(Post,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} {self.post}'

    class Meta:
        verbose_name = _('Комменты')
        verbose_name_plural = _('Коменты')
class CommentLike(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='user4')
    comment=models.OneToOneField(Comment,on_delete=models.CASCADE,related_name='comment')
    created_at =models.DateTimeField(auto_created=True,verbose_name='Дата создания')
    def __str__(self):
        return f'{self.user} {self.comment}'

    class Meta:
        verbose_name = _('Лайк на коммент')
        verbose_name_plural = _('Лайк на коммент')
class Story(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='user5')
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    video=models.FileField(upload_to='images/',blank=True,null=True)
    created_at =models.DateTimeField(auto_created=True,verbose_name='Дата создания')
    expires_at = models.DateTimeField()

    def __str__(self):
        return f'{self.user} {self.created_at}'

    class Meta:
        verbose_name = _('Сторис')
        verbose_name_plural = _('Сторис')

class Group(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField()
    creator=models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='creator')
    members=models.ManyToManyField(UserProfile)
    join_key=models.CharField(max_length=32,blank=True,null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группа')