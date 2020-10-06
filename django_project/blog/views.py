from django.shortcuts import render
from users.models import Profile
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {
        'jobs': Profile.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about-us.html', {'title': 'About'})


def user(request, pk):
    return render(request, 'blog/job-details.html')