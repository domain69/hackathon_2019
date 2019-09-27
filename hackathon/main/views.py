from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth


# Create your views here.
def index(request):
    return render(request,'main/index.html')

@login_required
def home(request):
    return render(request,'main/index.html')

def login(request):
    return render(request,'main/login.html')

@login_required
def settings(request):
    user = request.user

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None
    
    try:
        instagram_login = user.social_auth.get(provider='instagram')
    except UserSocialAuth.DoesNotExist:
        instagram_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    print(facebook_login,twitter_login,instagram_login)

    return render(request, 'main/setting.html', {
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'instagram_login':instagram_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('main:password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'main/password.html', {'form': form})