from django.urls import path
from . import views

app_name='userpages'
urlpatterns = [

   path('category/', views.category, name='category'),
   path('category_add/', views.category_add, name='category_add'),
   path('category_update/<category_id>', views.category_update, name='category_update'),
   path('delete_category/<category_id>', views.delete_category, name='delete_category'),
   path('job_add/', views.job_add, name='job_add'),
   path('job_update/<job_id>', views.job_update, name='job_update'),
   path('delete_job/<job_id>', views.delete_job, name='delete_job'),
   path('job/', views.job, name='job'),
   path('home/', views.home, name='home'),
]