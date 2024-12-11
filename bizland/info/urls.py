from django.urls import path
from . import views




app_name='info'

urlpatterns = [
    path("", views.index,name='index'),
    path("service-detail/<int:id>/", views.service_detail, name='service-detail'),
]


