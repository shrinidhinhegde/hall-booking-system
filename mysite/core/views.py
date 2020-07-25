from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewBooking
from .models import Booking


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    if request.method == 'POST':
        form = NewBooking(request.POST)
        if form.is_valid():
            obj = form.save()
        return redirect('home')
    else:
        form = NewBooking()
        display = Booking.objects.all()
        return render(request, 'secret_page.html', {'form': form,'list':display})
