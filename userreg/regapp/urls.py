from .import views

from django.urls import path
from .views import register_user, get_user_details

urlpatterns = [

    path('register/', register_user, name='register_user'),
    path('user-details/', get_user_details, name='user_details'),
]
