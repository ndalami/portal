from django.urls import path
from . import views

app_name='jobs'
urlpatterns = [
    path('detail/<job_id>',views.detail, name = 'detail'),
    path('jobs/',views.home, name = 'home'),
    path('',views.index, name = 'index_page'),
    path('search_job/',views.search_job, name = 'search'),
   
]
