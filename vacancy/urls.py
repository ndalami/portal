from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jobs.urls')),
    path('verifieds/',include('django.contrib.auth.urls')),
    path('verifieds/',include('verifieds.urls')),
    path('userpages/',include('userpages.urls')),
]

admin.site.site_header = 'WIBO Administration'