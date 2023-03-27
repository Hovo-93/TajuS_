from django.shortcuts import render
from usersdata.models import *


# Create your views here.
def users_with_passport(request):
    users_with_passport = User.objects.filter(passport__isnull=False).distinct()
    context = {
        'users_with_passport': users_with_passport
    }
    return render(request, 'users_with_passport.html', context)
