from django.urls import path
from . import views

app_name='verifieds'
urlpatterns = [
   path('verifieds/',views.verified_member, name = 'valid_member'),
   path('logout_user/',views.logout_user, name = 'logout'),
]
