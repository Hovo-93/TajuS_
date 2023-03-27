from django.urls import path, include
from usersdata.views import users_with_passport

urlpatterns = [

    path('', users_with_passport,name='user_with_passport'),

]