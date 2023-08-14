from django.shortcuts import render, redirect
from listing.models import Category, Listing
from django.contrib import messages

from .forms import SignupForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required



def index(request):
    listings = Listing.objects.filter(is_full=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'listings': listings,
    })




def contact(request):
    return render(request, 'core/contact.html')




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('core:profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)

    return render(request, 'core/profile.html', {'user_form': user_form, 'profile_form': profile_form})
