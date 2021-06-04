from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pendaftaran/', views.pendaftaran, name='Pendaftaran'),
    path('datasambang/', views.datasambang, name='Datasambang'),
    path('dataquota/', views.dataquota, name='Dataquota'),

]
