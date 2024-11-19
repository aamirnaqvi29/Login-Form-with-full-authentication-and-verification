from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/',register_attempt,name='register'),
    path('login/',login_attempt,name='login'),
    path('sucess/',sucess,name='sucess'),
    path('token/',token_send,name='token'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error/',error_page,name='error'),
]
