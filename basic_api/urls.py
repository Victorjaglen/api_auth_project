from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import item_list, register_user

urlpatterns = [
    path('items/', item_list, name='item-list'),
    path('register/', register_user, name='register-user'),
    path('login/', obtain_auth_token, name='login'),
]
