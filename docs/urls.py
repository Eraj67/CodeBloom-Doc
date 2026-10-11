from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/<int:pk>/', views.doc_detail, name='doc_detail'),

]