from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ClienteList.as_view()),
    path('<int:pk>/', views.ClienteDetail.as_view()),
]
