from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import UserProfile


class MyCustomSignupForm(SignupForm):
    bio=forms.CharField(max_length=100, label=_('bio'))
    image=forms.ImageField(label=_('image'))
    website=forms.CharField(max_length=20,label=_('website'))
    followers=forms.IntegerField(label=_('followers'))
    def save(self, request):
        user=super(MyCustomSignupForm,self).save(request)

        bio=self.cleaned_data['bio']
        image=self.cleaned_data['image']
        website=self.cleaned_data['website']
        followers=self.cleaned_data['followers']
        if hasattr(user,'userprofile'):
            profile=user.userprofile
        else:
            profile=UserProfile(user=user)

        profile.bio=bio
        profile.image=image
        profile.website=website
        profile.followers=followers
        profile.save()

        return user