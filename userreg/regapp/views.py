
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm
from .models import User, UserProfile

def demo(request):
    return render(request,"base.html")

def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('user_details')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def get_user_details(request):
    users = User.objects.all()
    return render(request, 'user_details.html', {'users': users})
