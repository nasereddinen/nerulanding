from django.urls import path
from . import views

app_name = 'bcb'

urlpatterns = [
    path('bcbvideosoftware/', views.bcbvideosoftware, name='index'),
    path('bcbprojectmanagment/', views.bcbprojectmanagment,
         name='bcbprojectmanagment'),
    path('bcbcrmsoftware/', views.bcbcrmsoftware, name='bcbcrmsoftware'),
    path('bcbappointment/',
         views.bcbappointmentsoftware, name="appointment"),
    path('bcbfilesharing/', views.bcbfilesharing, name='bcbfilesharingsoftware'),
    path('bcbvideoconfrencing/', views.bcbvideoconferencing, name='bcbvideoconferencing'),
    path('bcbaccounting/', views.bcbaccountingsoftware, name='bcbaccountingsoftware'),
    path('bcbtextmarketing/', views.bcbtextmarketing, name='bcbtextmarketing'),
    path('bcbvoice/', views.bcbvoice, name='bcbvoice'),
    path('bcbmarketingautomation/', views.bcbmarketingautomation, name='bcbmarketingautomation'),
    path('bcbwebsitebuilder/', views.bcbwebsitebuilder, name='bcbwebsitebuilder'),
    path('bcbwebhostingsoftware/', views.bcbwebhosting, name='bcbwebhosting'),
    path('bcbseosoftware/', views.bcbseosoftware, name='bcbseosoftware'),
]
