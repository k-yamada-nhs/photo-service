from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']

            new_user = authenticate(
                username=input_username, password=input_password)

            if new_user is not None:
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
