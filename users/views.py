from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are able to log in')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		user_update_form = UserUpdateForm(request.POST, instance=request.user)
		profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
		if user_update_form.is_valid() and profile_update_form.is_valid():
			user_update_form.save()
			profile_update_form.save()
			messages.success(request, 'Your Profile has been updated')
			return redirect('profile')
	else:
		user_update_form = UserUpdateForm(instance=request.user)
		profile_update_form = ProfileUpdateForm(instance=request.user)

	context = {
		'user_update_form': user_update_form,
		'profile_update_form': profile_update_form
	}
	return render(request, 'users/profile.html', context)
