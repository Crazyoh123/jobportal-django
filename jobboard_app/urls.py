from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_job_posting, name='create_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.view_job, name='view_job'),
]
